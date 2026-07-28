"""
DiskArchive Pro v2
Analysis Service
"""

from app.repository.disk_repository import DiskRepository
from app.repository.folder_repository import FolderRepository
from app.repository.file_repository import FileRepository


class AnalysisService:

    def __init__(self, db):

        self.disk_repository = DiskRepository(db)
        self.folder_repository = FolderRepository(db)
        self.file_repository = FileRepository(db)

    # -------------------------------------------------
    # OVERVIEW
    # -------------------------------------------------

    def overview(self):

        return {

            "disk_count": self.disk_repository.count(),

            "folder_count": self.folder_repository.count(),

            "file_count": self.file_repository.count(),

            "total_size": self.file_repository.total_size(),

            "empty_folders": self.folder_repository.empty_count(),

            "empty_files": self.file_repository.empty_count(),

        }

    # -------------------------------------------------
    # LARGEST FILES
    # -------------------------------------------------

    def largest_files(self, limit=20):

        return self.file_repository.get_largest(limit)

    # -------------------------------------------------
    # LARGEST FOLDERS
    # -------------------------------------------------

    def largest_folders(self, limit=20):

        return self.folder_repository.get_largest(limit)

    # -------------------------------------------------
    # EMPTY FILES
    # -------------------------------------------------

    def empty_files(self):

        return self.file_repository.empty_count()

    # -------------------------------------------------
    # EMPTY FOLDERS
    # -------------------------------------------------

    def empty_folders(self):

        return self.folder_repository.empty_count()

    # -------------------------------------------------
    # FILE TYPES
    # -------------------------------------------------

    def extension_statistics(self):

        return self.file_repository.extension_statistics()

    # -------------------------------------------------
    # TOTAL SIZE
    # -------------------------------------------------

    def total_size(self):

        return self.file_repository.total_size()

    # -------------------------------------------------
    # DUPLICATE FILES
    # (Hazır - ileride geliştirilecek)
    # -------------------------------------------------

    def duplicate_files(self):

        return []

    # -------------------------------------------------
    # VIDEO FILES
    # -------------------------------------------------

    def video_files(self):

        extensions = [
            ".mp4",
            ".mkv",
            ".avi",
            ".mov",
            ".wmv",
            ".flv",
        ]

        result = []

        for ext in extensions:

            result.extend(

                self.file_repository.search(

                    {

                        "name": None,

                        "extension": ext,

                        "disk": None,

                        "min_size": None,

                        "max_size": None,

                        "date": None,

                    }

                )

            )

        return result

    # -------------------------------------------------
    # ARCHIVE FILES
    # -------------------------------------------------

    def archive_files(self):

        extensions = [
            ".zip",
            ".rar",
            ".7z",
            ".tar",
            ".gz",
        ]

        result = []

        for ext in extensions:

            result.extend(

                self.file_repository.search(

                    {

                        "name": None,

                        "extension": ext,

                        "disk": None,

                        "min_size": None,

                        "max_size": None,

                        "date": None,

                    }

                )

            )

        return result

    # -------------------------------------------------
    # ISO / VIRTUAL DISKS
    # -------------------------------------------------

    def virtual_disks(self):

        extensions = [
            ".iso",
            ".vhd",
            ".vhdx",
            ".vmdk",
            ".vdi",
        ]

        result = []

        for ext in extensions:

            result.extend(

                self.file_repository.search(

                    {

                        "name": None,

                        "extension": ext,

                        "disk": None,

                        "min_size": None,

                        "max_size": None,

                        "date": None,

                    }

                )

            )

        return result