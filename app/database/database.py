"""
DiskArchive Pro v2
Database Manager
"""

import sqlite3

from app.config.config import Config
from app.database.schema import create_database
from app.utils.logger import Logger


class Database:

    def __init__(self):

        Config.initialize()

        self.connection = sqlite3.connect(
            Config.DATABASE_FILE,
            timeout=Config.DATABASE_TIMEOUT,
            check_same_thread=False,
        )

        self.connection.row_factory = sqlite3.Row

        self.initialize()

    # -------------------------------------------------
    # INITIALIZE
    # -------------------------------------------------

    def initialize(self):

        cursor = self.connection.cursor()

        cursor.execute("PRAGMA foreign_keys = ON;")
        cursor.execute("PRAGMA journal_mode = WAL;")
        cursor.execute("PRAGMA synchronous = NORMAL;")
        cursor.execute("PRAGMA temp_store = MEMORY;")
        cursor.execute("PRAGMA cache_size = -100000;")

        create_database(self.connection)

        self.connection.commit()

        Logger.info("Database initialized.")

    # -------------------------------------------------
    # EXECUTE
    # -------------------------------------------------

    def execute(self, sql, parameters=()):

        cursor = self.connection.cursor()

        cursor.execute(sql, parameters)

        return cursor

    # -------------------------------------------------
    # EXECUTEMANY
    # -------------------------------------------------

    def executemany(self, sql, values):

        cursor = self.connection.cursor()

        cursor.executemany(sql, values)

        return cursor

    # -------------------------------------------------
    # FETCH ONE
    # -------------------------------------------------

    def fetchone(self, sql, parameters=()):

        return self.execute(
            sql,
            parameters,
        ).fetchone()

    # -------------------------------------------------
    # FETCH ALL
    # -------------------------------------------------

    def fetchall(self, sql, parameters=()):

        return self.execute(
            sql,
            parameters,
        ).fetchall()

    # -------------------------------------------------
    # SCALAR
    # -------------------------------------------------

    def scalar(self, sql, parameters=()):

        row = self.fetchone(
            sql,
            parameters,
        )

        return row[0] if row else None

    # -------------------------------------------------
    # BEGIN
    # -------------------------------------------------

    def begin(self):

        self.connection.execute("BEGIN")

    # -------------------------------------------------
    # COMMIT
    # -------------------------------------------------

    def commit(self):

        self.connection.commit()

    # -------------------------------------------------
    # ROLLBACK
    # -------------------------------------------------

    def rollback(self):

        self.connection.rollback()

    # -------------------------------------------------
    # VACUUM
    # -------------------------------------------------

    def vacuum(self):

        self.connection.execute("VACUUM")

        self.connection.commit()

        Logger.info("Database vacuum completed.")

    # -------------------------------------------------
    # ANALYZE
    # -------------------------------------------------

    def analyze(self):

        self.connection.execute("ANALYZE")

        self.connection.commit()

        Logger.info("Database analyze completed.")

    # -------------------------------------------------
    # BACKUP
    # -------------------------------------------------

    def backup(self, destination):

        backup = sqlite3.connect(destination)

        self.connection.backup(backup)

        backup.close()

        Logger.info(
            f"Database backup created: {destination}"
        )

    # -------------------------------------------------
    # CLOSE
    # -------------------------------------------------

    def close(self):

        if self.connection:

            self.connection.close()

            Logger.info("Database closed.")

    # -------------------------------------------------
    # CONTEXT MANAGER
    # -------------------------------------------------

    def __enter__(self):

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):

        if exc_type:

            Logger.exception(
                "Database transaction failed."
            )

            self.rollback()

        else:

            self.commit()

        self.close()