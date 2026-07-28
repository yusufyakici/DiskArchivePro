"""
DiskArchive Pro v2
Scan Worker
"""

from PySide6.QtCore import QObject
from PySide6.QtCore import Signal
from PySide6.QtCore import Slot

from app.services.disk_service import DiskService
from app.utils.logger import Logger


class ScanWorker(QObject):

    # -------------------------------------------------
    # SIGNALS
    # -------------------------------------------------

    started = Signal()

    progress = Signal(int)

    status = Signal(str)

    finished = Signal(dict)

    error = Signal(str)

    # -------------------------------------------------
    # INIT
    # -------------------------------------------------

    def __init__(self, db, path):

        super().__init__()

        self.db = db

        self.path = path

        self.service = DiskService(db)

    # -------------------------------------------------
    # RUN
    # -------------------------------------------------

    @Slot()
    def run(self):

        try:

            Logger.info(
                f"Worker started : {self.path}"
            )

            self.started.emit()

            #
            # Callback'leri bağla
            #

            self.service.engine.set_callbacks(

                progress=self.progress.emit,

                status=self.status.emit,

            )

            #
            # Tarama
            #

            statistics = self.service.scan(self.path)

            if statistics is None:
                statistics = {}

            self.finished.emit(statistics)

            Logger.info(
                "ScanWorker tamamlandı."
            )

        except Exception as e:

            Logger.exception(str(e))

            self.error.emit(
                str(e)
            )