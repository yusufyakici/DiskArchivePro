"""
DiskArchive Pro v2
Database Schema
"""

from app.config.config import Config

# =====================================================
# DISKS
# =====================================================

CREATE_DISKS_TABLE = """
CREATE TABLE IF NOT EXISTS disks
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    label TEXT NOT NULL,
    drive_letter TEXT NOT NULL UNIQUE,
    serial_number TEXT,
    file_system TEXT,

    capacity INTEGER DEFAULT 0,
    used_space INTEGER DEFAULT 0,
    free_space INTEGER DEFAULT 0,

    scan_date TEXT NOT NULL
);
"""

# =====================================================
# FOLDERS
# =====================================================

CREATE_FOLDERS_TABLE = """
CREATE TABLE IF NOT EXISTS folders
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    disk_id INTEGER NOT NULL,
    parent_id INTEGER,

    name TEXT NOT NULL,
    path TEXT NOT NULL UNIQUE,

    size INTEGER DEFAULT 0,
    file_count INTEGER DEFAULT 0,
    folder_count INTEGER DEFAULT 0,

    created_at TEXT,
    modified_at TEXT,

    FOREIGN KEY(disk_id)
        REFERENCES disks(id)
        ON DELETE CASCADE,

    FOREIGN KEY(parent_id)
        REFERENCES folders(id)
        ON DELETE CASCADE
);
"""

# =====================================================
# FILES
# =====================================================

CREATE_FILES_TABLE = """
CREATE TABLE IF NOT EXISTS files
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    disk_id INTEGER NOT NULL,
    folder_id INTEGER NOT NULL,

    name TEXT NOT NULL,
    extension TEXT,
    full_path TEXT NOT NULL UNIQUE,

    size INTEGER DEFAULT 0,

    created_at TEXT,
    modified_at TEXT,

    hash TEXT,

    FOREIGN KEY(disk_id)
        REFERENCES disks(id)
        ON DELETE CASCADE,

    FOREIGN KEY(folder_id)
        REFERENCES folders(id)
        ON DELETE CASCADE
);
"""

# =====================================================
# SCAN HISTORY
# =====================================================

CREATE_SCAN_HISTORY_TABLE = """
CREATE TABLE IF NOT EXISTS scan_history
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    scan_date TEXT NOT NULL,
    scanned_path TEXT NOT NULL,

    disk_count INTEGER DEFAULT 0,
    folder_count INTEGER DEFAULT 0,
    file_count INTEGER DEFAULT 0,

    total_size INTEGER DEFAULT 0,

    duration REAL DEFAULT 0,

    status TEXT DEFAULT 'Completed'
);
"""

# =====================================================
# EXTENSIONS
# =====================================================

CREATE_EXTENSIONS_TABLE = """
CREATE TABLE IF NOT EXISTS extensions
(
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    extension TEXT NOT NULL UNIQUE,

    file_count INTEGER DEFAULT 0,

    total_size INTEGER DEFAULT 0
);
"""

# =====================================================
# SETTINGS
# =====================================================

CREATE_SETTINGS_TABLE = """
CREATE TABLE IF NOT EXISTS settings
(
    key TEXT PRIMARY KEY,

    value TEXT
);
"""

# =====================================================
# FULL TEXT SEARCH
# =====================================================

CREATE_FILES_FTS = """
CREATE VIRTUAL TABLE IF NOT EXISTS files_fts
USING fts5
(
    name,
    full_path,
    extension
);
"""

# =====================================================
# INDEXES
# =====================================================

CREATE_INDEXES = [

    # -------------------------
    # DISKS
    # -------------------------

    """
    CREATE INDEX IF NOT EXISTS idx_disk_drive
    ON disks(drive_letter);
    """,

    # -------------------------
    # FOLDERS
    # -------------------------

    """
    CREATE INDEX IF NOT EXISTS idx_folder_disk
    ON folders(disk_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_folder_parent
    ON folders(parent_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_folder_path
    ON folders(path);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_folder_name
    ON folders(name);
    """,

    # -------------------------
    # FILES
    # -------------------------

    """
    CREATE INDEX IF NOT EXISTS idx_file_disk
    ON files(disk_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_folder
    ON files(folder_id);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_name
    ON files(name);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_extension
    ON files(extension);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_path
    ON files(full_path);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_size
    ON files(size);
    """,

    """
    CREATE INDEX IF NOT EXISTS idx_file_hash
    ON files(hash);
    """,

    # -------------------------
    # SCAN HISTORY
    # -------------------------

    """
    CREATE INDEX IF NOT EXISTS idx_scan_date
    ON scan_history(scan_date);
    """
]

# =====================================================
# CREATE DATABASE
# =====================================================

def create_database(connection):

    cursor = connection.cursor()

    # -------------------------------------------------
    # Tables
    # -------------------------------------------------

    cursor.execute(CREATE_DISKS_TABLE)
    cursor.execute(CREATE_FOLDERS_TABLE)
    cursor.execute(CREATE_FILES_TABLE)
    cursor.execute(CREATE_SCAN_HISTORY_TABLE)
    cursor.execute(CREATE_EXTENSIONS_TABLE)
    cursor.execute(CREATE_SETTINGS_TABLE)

    # -------------------------------------------------
    # Full Text Search
    # -------------------------------------------------

    if Config.ENABLE_FTS:
        cursor.execute(CREATE_FILES_FTS)

    # -------------------------------------------------
    # Indexes
    # -------------------------------------------------

    for sql in CREATE_INDEXES:
        cursor.execute(sql)

    connection.commit()