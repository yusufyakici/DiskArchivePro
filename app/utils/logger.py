"""
DiskArchive Pro v2
Application Logger
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from app.config.config import Config


class Logger:

    _logger = None

    # -------------------------------------------------
    # INITIALIZE
    # -------------------------------------------------

    @classmethod
    def initialize(cls):

        if cls._logger is not None:
            return

        Config.initialize()

        log_file = Path(Config.LOG_DIR) / "diskarchive.log"

        cls._logger = logging.getLogger("DiskArchive")

        cls._logger.setLevel(
            getattr(
                logging,
                Config.LOG_LEVEL.upper(),
                logging.INFO,
            )
        )

        cls._logger.handlers.clear()

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
            "%Y-%m-%d %H:%M:%S",
        )

        # -------------------------------------------------
        # File Handler
        # -------------------------------------------------

        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=10 * 1024 * 1024,   # 10 MB
            backupCount=5,
            encoding="utf-8",
        )

        file_handler.setFormatter(formatter)

        cls._logger.addHandler(file_handler)

        # -------------------------------------------------
        # Console Handler
        # -------------------------------------------------

        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        cls._logger.addHandler(console_handler)

        cls._logger.propagate = False

        cls.info("Logger initialized.")

    # -------------------------------------------------
    # GET LOGGER
    # -------------------------------------------------

    @classmethod
    def get_logger(cls):

        cls.initialize()

        return cls._logger

    # -------------------------------------------------
    # DEBUG
    # -------------------------------------------------

    @classmethod
    def debug(cls, message):

        cls.initialize()

        cls._logger.debug(message)

    # -------------------------------------------------
    # INFO
    # -------------------------------------------------

    @classmethod
    def info(cls, message):

        cls.initialize()

        cls._logger.info(message)

    # -------------------------------------------------
    # WARNING
    # -------------------------------------------------

    @classmethod
    def warning(cls, message):

        cls.initialize()

        cls._logger.warning(message)

    # -------------------------------------------------
    # ERROR
    # -------------------------------------------------

    @classmethod
    def error(cls, message):

        cls.initialize()

        cls._logger.error(message)

    # -------------------------------------------------
    # CRITICAL
    # -------------------------------------------------

    @classmethod
    def critical(cls, message):

        cls.initialize()

        cls._logger.critical(message)

    # -------------------------------------------------
    # EXCEPTION
    # -------------------------------------------------

    @classmethod
    def exception(cls, message):

        cls.initialize()

        cls._logger.exception(message)