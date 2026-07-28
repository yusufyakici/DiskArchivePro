"""
DiskArchive Pro v2
Search Service
"""

from app.repository.file_repository import FileRepository
from app.repository.folder_repository import FolderRepository
from app.services.search_parser import SearchParser


class SearchService:

    def __init__(self, db):

        self.db = db

        self.file_repository = FileRepository(db)

        self.folder_repository = FolderRepository(db)

        self.parser = SearchParser()

    # -------------------------------------------------
    # FILE SEARCH
    # -------------------------------------------------

    def search_files(self, text):

        filters = self.parser.parse(text)

        return self.file_repository.search(
            filters
        )

    # -------------------------------------------------
    # FOLDER SEARCH
    # -------------------------------------------------

    def search_folders(self, text):

        keyword = text.strip()

        if not keyword:
            return []

        return self.folder_repository.search(
            keyword
        )

    # -------------------------------------------------
    # GLOBAL SEARCH
    # -------------------------------------------------

    def search(self, text):

        return {

            "files": self.search_files(text),

            "folders": self.search_folders(text),

        }

    # -------------------------------------------------
    # SEARCH BY EXTENSION
    # -------------------------------------------------

    def search_extension(self, extension):

        return self.file_repository.search(
            {
                "name": None,
                "extension": extension.lower(),
                "min_size": None,
                "max_size": None,
                "date": None,
            }
        )

    # -------------------------------------------------
    # SEARCH LARGE FILES
    # -------------------------------------------------

    def search_large_files(self, minimum_size):

        return self.file_repository.search(
            {
                "name": None,
                "extension": None,
                "min_size": minimum_size,
                "max_size": None,
                "date": None,
            }
        )

    # -------------------------------------------------
    # RECENT FILES
    # -------------------------------------------------

    def search_recent(self, year):

        return self.file_repository.search(
            {
                "name": None,
                "extension": None,
                "min_size": None,
                "max_size": None,
                "date": str(year),
            }
        )

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear(self):

        return {
            "files": [],
            "folders": [],
        }