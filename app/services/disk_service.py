"""
DiskArchive Pro v2
Disk Service
"""

from pathlib import Path
import os

from app.scanner.scan_engine import ScanEngine

from app.repository.disk_repository import DiskRepository
from app.repository.folder_repository import FolderRepository
from app.repository.file_repository import FileRepository

from app.utils.logger import Logger


class DiskService:

    # -------------------------------------------------
    # INIT
    # -------------------------------------------------

    def __init__(self, db):

        self.db = db

        self.engine = ScanEngine()

        self.disk_repository = DiskRepository(db)

        self.folder_repository = FolderRepository(db)

        self.file_repository = FileRepository(db)
    # -------------------------------------------------
    # SCAN
    # -------------------------------------------------

    def scan(self, path):

        Logger.info(
            f"Tarama başladı : {path}"
        )

        #
        # Database
        #

        self.clear_database()

        #
        # Scan
        #

        self.engine.scan(path)

        #
        # Disk
        #

        disk = self.save_disk()

        #
        # Folder
        #

        folder_map = self.save_folders(
            disk.id
        )

        #
        # Files
        #

        self.save_files(

            disk.id,

            folder_map,

        )

        #
        # Commit
        #

        self.db.commit()

        Logger.info(
            "Tarama tamamlandı."
        )

        return self.engine.get_statistics()
    # -------------------------------------------------
    # SAVE DISK
    # -------------------------------------------------

    def save_disk(self):

        disk = self.engine.disk

        if disk is None:

            raise RuntimeError(
                "Disk oluşturulamadı."
            )

        disk = self.disk_repository.save(
            disk
        )

        Logger.info(
            f"Disk kaydedildi : {disk.drive_letter}"
        )

        return disk

    # -------------------------------------------------
    # SAVE FOLDERS
    # -------------------------------------------------

    def save_folders(self, disk_id):

        #
        # Disk ID
        #

        for folder in self.engine.folders:

            folder.disk_id = disk_id

        #
        # Save
        #

        folder_map = self.folder_repository.save_all(
            self.engine.folders
        )

        #
        # Parent ID
        #

        for folder in self.engine.folders:

            parent_path = os.path.normcase(
                os.path.normpath(
                    str(Path(folder.path).parent)
                )
            )

            folder.parent_id = folder_map.get(
                parent_path
            )

        #
        # Update Parent IDs
        #

        self.folder_repository.update_parent_ids(
            self.engine.folders
        )

        Logger.info(
            f"Klasör kaydedildi : {len(folder_map)}"
        )

        return folder_map
    # -------------------------------------------------
    # SAVE FILES
    # -------------------------------------------------

    def save_files(self, disk_id, folder_map):

        files = self.engine.files

        if not files:

            Logger.warning(
                "Kaydedilecek dosya bulunamadı."
            )
            return

        #
        # Disk ID / Folder ID
        #

        for file in files:

            file.disk_id = disk_id

            folder_path = os.path.normcase(
                os.path.normpath(
                    str(Path(file.full_path).parent)
                )
            )

            folder_id = folder_map.get(folder_path)

            if folder_id is None:

                Logger.warning(
                    f"Folder bulunamadı : {folder_path}"
                )

                continue

            file.folder_id = folder_id

        #
        # Save
        #

        self.file_repository.add_many(files)

        Logger.info(
            f"Dosya kaydedildi : {len(files)}"
        )
    # -------------------------------------------------
    # CLEAR DATABASE
    # -------------------------------------------------

    def clear_database(self):

        Logger.info(
            "Veritabanı temizleniyor..."
        )

        #
        # Önce child tablolar
        #

        self.file_repository.clear()

        self.folder_repository.clear()

        self.disk_repository.clear()

        self.db.commit()

        Logger.info(

            "Veritabanı temizlendi."

        )

    # -------------------------------------------------
    # STATISTICS
    # -------------------------------------------------

    def statistics(self):

        return self.engine.get_statistics()