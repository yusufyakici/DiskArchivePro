"""
DiskArchive Pro v2
Helpers
"""

from pathlib import Path


class Helpers:

    # -------------------------------------------------
    # FILE EXTENSION
    # -------------------------------------------------

    @staticmethod
    def extension(path):

        return Path(path).suffix.lower()

    # -------------------------------------------------
    # FILE NAME
    # -------------------------------------------------

    @staticmethod
    def filename(path):

        return Path(path).name

    # -------------------------------------------------
    # FOLDER NAME
    # -------------------------------------------------

    @staticmethod
    def folder(path):

        return Path(path).parent.name

    # -------------------------------------------------
    # EXISTS
    # -------------------------------------------------

    @staticmethod
    def exists(path):

        return Path(path).exists()

    # -------------------------------------------------
    # IS FILE
    # -------------------------------------------------

    @staticmethod
    def is_file(path):

        return Path(path).is_file()

    # -------------------------------------------------
    # IS DIR
    # -------------------------------------------------

    @staticmethod
    def is_dir(path):

        return Path(path).is_dir()