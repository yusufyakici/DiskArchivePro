"""
DiskArchive Pro v2
Scan Engine
"""

from datetime import datetime
from pathlib import Path
import os

from app.config.config import Config
from app.models.disk import Disk
from app.models.folder import Folder
from app.models.file import File
from app.utils.logger import Logger


class ScanEngine:

    # -------------------------------------------------
    # INIT
    # -------------------------------------------------

    def __init__(self):

        #
        # Callbacks
        #

        self.progress_callback = None
        self.status_callback = None

        #
        # Cancel
        #

        self.cancel_requested = False

        #
        # Reset
        #

        self.reset()

    # -------------------------------------------------
    # RESET
    # -------------------------------------------------

    def reset(self):

        #
        # Cancel
        #

        self.cancel_requested = False

        #
        # Disk
        #

        self.disk = None

        #
        # Cache
        #

        self.folder_cache = {}

        self.file_cache = {}

        #
        # Statistics
        #

        self.statistics = {

            "folder_count": 0,
            "file_count": 0,
            "total_size": 0,

            "start_time": None,
            "finish_time": None,

        }

    # -------------------------------------------------
    # CALLBACKS
    # -------------------------------------------------

    def set_callbacks(

        self,

        progress=None,

        status=None,

    ):

        self.progress_callback = progress

        self.status_callback = status

    # -------------------------------------------------
    # CANCEL
    # -------------------------------------------------

    def cancel(self):

        self.cancel_requested = True

        Logger.info(
            "Tarama iptali istendi."
        )
    # -------------------------------------------------
    # SCAN
    # -------------------------------------------------

    def scan(self, root_path):

        #
        # Reset
        #

        self.reset()

        root = Path(root_path).resolve()

        Logger.info(
            f"Taranıyor : {root}"
        )

        self.statistics["start_time"] = datetime.now()

        #
        # Disk
        #

        self.disk = Disk(

            label=root.name or str(root),

            drive_letter=str(root),

            scan_date=datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        )

        #
        # Scan
        #

        for current_path, dirs, files in os.walk(

            root,

            followlinks=Config.FOLLOW_SYMLINKS,

        ):

            #
            # Cancel
            #

            if self.cancel_requested:

                Logger.info(
                    "Tarama kullanıcı tarafından durduruldu."
                )

                break

            #
            # Folder
            #

            self.scan_folder(

                current_path,

                dirs,

                files,

            )

        #
        # Folder Sizes
        #

        self.calculate_folder_sizes()

        #
        # Disk Statistics
        #

        self.disk.capacity = self.statistics["total_size"]

        self.disk.used_space = self.statistics["total_size"]

        self.disk.free_space = 0

        #
        # Finish
        #

        self.statistics["finish_time"] = datetime.now()

        Logger.info(
            "Tarama tamamlandı."
        )
    # -------------------------------------------------
    # SCAN FOLDER
    # -------------------------------------------------

    def scan_folder(self, current_path, dirs, files):

        try:

            #
            # Normalize Path
            #

            path = Path(current_path).resolve()

            normalized_path = os.path.normcase(
                os.path.normpath(
                    str(path)
                )
            )

            #
            # Status
            #

            if self.status_callback:

                self.status_callback(
                    normalized_path
                )

            #
            # Folder Info
            #

            stat = path.stat()

            folder = Folder(

                disk_id=0,

                parent_id=None,

                name=path.name or str(path),

                path=normalized_path,

                size=0,

                file_count=len(files),

                folder_count=len(dirs),

                created_at=datetime.fromtimestamp(
                    stat.st_ctime
                ).strftime("%Y-%m-%d %H:%M:%S"),

                modified_at=datetime.fromtimestamp(
                    stat.st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S"),

            )

            #
            # Cache
            #

            self.folder_cache[
                normalized_path
            ] = folder

            #
            # Statistics
            #

            self.statistics["folder_count"] += 1

            #
            # Files
            #

            for filename in files:

                if self.cancel_requested:

                    return

                self.scan_file(

                    path / filename,

                    folder,

                )

        except Exception as e:

            Logger.warning(

                f"Klasör okunamadı : {current_path}\n{e}"

            )
    # -------------------------------------------------
    # SCAN FILE
    # -------------------------------------------------

    def scan_file(self, file_path, folder):

        try:

            #
            # Cancel
            #

            if self.cancel_requested:

                return

            #
            # Path
            #

            path = Path(file_path).resolve()

            normalized_path = os.path.normcase(
                os.path.normpath(
                    str(path)
                )
            )

            #
            # Duplicate Control
            #

            if normalized_path in self.file_cache:

                return

            #
            # File Info
            #

            stat = path.stat()

            size = stat.st_size

            #
            # File Model
            #

            file = File(

                disk_id=0,

                folder_id=0,

                name=path.name,

                extension=path.suffix.lower(),

                full_path=normalized_path,

                size=size,

                created_at=datetime.fromtimestamp(
                    stat.st_ctime
                ).strftime("%Y-%m-%d %H:%M:%S"),

                modified_at=datetime.fromtimestamp(
                    stat.st_mtime
                ).strftime("%Y-%m-%d %H:%M:%S"),

                hash="",

            )

            #
            # Cache
            #

            self.file_cache[
                normalized_path
            ] = file

            #
            # Folder Size
            #

            folder.size += size

            #
            # Statistics
            #

            self.statistics["file_count"] += 1

            self.statistics["total_size"] += size

            #
            # Progress
            #

            if self.progress_callback:

                self.progress_callback(

                    self.statistics["file_count"]

                )

        except PermissionError:

            Logger.warning(

                f"Erişim reddedildi : {file_path}"

            )

        except FileNotFoundError:

            Logger.warning(

                f"Dosya bulunamadı : {file_path}"

            )

        except Exception as e:

            Logger.warning(

                f"Dosya okunamadı : {file_path}\n{e}"

            )
    # -------------------------------------------------
    # CALCULATE FOLDER SIZES
    # -------------------------------------------------

    def calculate_folder_sizes(self):

        Logger.info(
            "Klasör boyutları hesaplanıyor..."
        )

        folders = sorted(

            self.folder_cache.values(),

            key=lambda folder: len(
                Path(folder.path).parts
            ),

            reverse=True,

        )

        for folder in folders:

            parent_path = os.path.normcase(
                os.path.normpath(
                    str(Path(folder.path).parent)
                )
            )

            parent = self.folder_cache.get(
                parent_path
            )

            if parent:

                parent.size += folder.size

        Logger.info(
            "Klasör boyutları hesaplandı."
        )

    # -------------------------------------------------
    # PROPERTIES
    # -------------------------------------------------

    @property
    def folders(self):

        return list(
            self.folder_cache.values()
        )

    @property
    def files(self):

        return list(
            self.file_cache.values()
        )

    # -------------------------------------------------
    # SCAN DURATION
    # -------------------------------------------------

    @property
    def scan_duration(self):

        start = self.statistics["start_time"]

        finish = self.statistics["finish_time"]

        if start is None or finish is None:

            return 0

        return round(

            (finish - start).total_seconds(),

            2,

        )

    # -------------------------------------------------
    # GET STATISTICS
    # -------------------------------------------------

    def get_statistics(self):

        stats = dict(
            self.statistics
        )

        stats["duration"] = self.scan_duration

        stats["average_file_size"] = (

            0

            if stats["file_count"] == 0

            else round(

                stats["total_size"]
                / stats["file_count"],

                2,

            )

        )

        stats["folder_size"] = sum(

            folder.size

            for folder in self.folder_cache.values()

        )

        return stats