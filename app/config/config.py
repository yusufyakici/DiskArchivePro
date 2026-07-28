"""
DiskArchive Pro v2
Application Configuration
"""
import os
from pathlib import Path


class Config:

    # -------------------------------------------------
    # APPLICATION
    # -------------------------------------------------

    APP_NAME = "DiskArchive Pro"

    VERSION = "2.0.0"

    ORGANIZATION = "Yusuf Yakıcı Software"

    # -------------------------------------------------
    # WINDOW
    # -------------------------------------------------

    WINDOW_TITLE = f"{APP_NAME} v{VERSION}"

    WINDOW_WIDTH = 1400

    WINDOW_HEIGHT = 900

    # -------------------------------------------------
    # DIRECTORIES
    # -------------------------------------------------

    ROOT_DIR = Path(__file__).resolve().parents[2]

    DATA_DIR = ROOT_DIR / "data"

    EXPORT_DIR = ROOT_DIR / "exports"

    LOG_DIR = ROOT_DIR / "logs"

    ASSET_DIR = ROOT_DIR / "assets"

    DATABASE_FILE = DATA_DIR / "diskarchive.db"

    # -------------------------------------------------
    # SCAN
    # -------------------------------------------------

    HASH_FILES = False

    FOLLOW_SYMLINKS = False

    MAX_BATCH_SIZE = 5000

    # -------------------------------------------------
    # REPORTS
    # -------------------------------------------------

    PDF_ENABLED = True

    EXCEL_ENABLED = True

    CSV_ENABLED = True

    HTML_ENABLED = True

    # -------------------------------------------------
    # GUI
    # -------------------------------------------------

    DEFAULT_THEME = "dark"

    DEFAULT_LANGUAGE = "tr"

    # -------------------------------------------------
    # INITIALIZE
    # -------------------------------------------------

    @classmethod
    def initialize(cls):

        cls.DATA_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        cls.EXPORT_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        cls.LOG_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        cls.ASSET_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )
    # -------------------------------------------------
    # PERFORMANCE
    # -------------------------------------------------

    MAX_RESULTS = 500

    AUTO_COMMIT = False

    THREAD_COUNT = max(2, os.cpu_count() or 4)

    # -------------------------------------------------
    # LOGGING
    # -------------------------------------------------

    LOG_LEVEL = "INFO"

    # -------------------------------------------------
    # DATABASE
    # -------------------------------------------------

    DATABASE_TIMEOUT = 30

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    ENABLE_FTS = True

    # -------------------------------------------------
    # SCAN
    # -------------------------------------------------

    SKIP_HIDDEN_FILES = False

    SKIP_SYSTEM_FILES = False