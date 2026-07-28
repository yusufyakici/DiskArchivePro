"""
DiskArchive Pro v2
Dashboard Service
"""

from app.repository.disk_repository import DiskRepository
from app.repository.folder_repository import FolderRepository
from app.repository.file_repository import FileRepository


class DashboardService:

    def __init__(self, db):

        self.disk_repository = DiskRepository(db)
        self.folder_repository = FolderRepository(db)
        self.file_repository = FileRepository(db)

    # -------------------------------------------------
    # DASHBOARD STATISTICS
    # -------------------------------------------------

    def get_statistics(self):

        return {

            "disk_count": self.disk_repository.count(),

            "folder_count": self.folder_repository.count(),

            "file_count": self.file_repository.count(),

            "total_file_size": self.file_repository.total_size(),

            "empty_folder_count": self.folder_repository.empty_count(),

            "empty_file_count": self.file_repository.empty_count(),

        }

    # -------------------------------------------------
    # DISKS
    # -------------------------------------------------

    def get_disks(self):

        return self.disk_repository.get_all()

    # -------------------------------------------------
    # LAST SCANNED DISK
    # -------------------------------------------------

    def get_last_disk(self):

        return self.disk_repository.get_last_scanned()

    # -------------------------------------------------
    # LARGEST FOLDERS
    # -------------------------------------------------

    def get_largest_folders(self, limit=10):

        return self.folder_repository.get_largest(limit)

    # -------------------------------------------------
    # LARGEST FILES
    # -------------------------------------------------

    def get_largest_files(self, limit=10):

        return self.file_repository.get_largest(limit)

    # -------------------------------------------------
    # EMPTY FOLDERS
    # -------------------------------------------------

    def get_empty_folder_count(self):

        return self.folder_repository.empty_count()

    # -------------------------------------------------
    # EMPTY FILES
    # -------------------------------------------------

    def get_empty_file_count(self):

        return self.file_repository.empty_count()

    # -------------------------------------------------
    # FILE TYPES
    # -------------------------------------------------

    def get_extension_statistics(self):

        return self.file_repository.extension_statistics()

    # -------------------------------------------------
    # TOTAL SIZE
    # -------------------------------------------------

    def get_total_size(self):

        return self.file_repository.total_size()