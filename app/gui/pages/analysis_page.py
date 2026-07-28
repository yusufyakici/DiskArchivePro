"""
DiskArchive Pro v2
Analysis Page
"""

from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QSplitter,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from app.gui.widgets.card_widget import CardWidget
from app.gui.widgets.chart_widget import ChartWidget
from app.gui.widgets.file_table import FileTable
from app.gui.widgets.folder_tree import FolderTree

from app.services.analysis_service import AnalysisService
from app.utils.formatter import format_size


class AnalysisPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.service = AnalysisService(db)

        self.setup_ui()

        self.refresh()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Kartlar
        #

        self.file_card = CardWidget("Dosya", "0")
        self.folder_card = CardWidget("Klasör", "0")
        self.size_card = CardWidget("Toplam Boyut", "0 B")
        self.empty_card = CardWidget("Boş Klasör", "0")

        cards = QGridLayout()

        cards.addWidget(self.file_card, 0, 0)
        cards.addWidget(self.folder_card, 0, 1)
        cards.addWidget(self.size_card, 0, 2)
        cards.addWidget(self.empty_card, 0, 3)

        #
        # Büyük Dosyalar
        #

        self.file_table = FileTable()

        #
        # Büyük Klasörler
        #

        self.folder_tree = FolderTree()

        #
        # Analiz Sekmeleri
        #

        self.video_table = FileTable()
        self.archive_table = FileTable()
        self.virtual_table = FileTable()

        self.tabs = QTabWidget()

        self.tabs.addTab(
            self.video_table,
            "Video"
        )

        self.tabs.addTab(
            self.archive_table,
            "Arşiv"
        )

        self.tabs.addTab(
            self.virtual_table,
            "ISO / Sanal Disk"
        )

        #
        # Grafik
        #

        self.chart = ChartWidget()

        #
        # Sol Panel
        #

        left = QWidget()

        left_layout = QVBoxLayout(left)

        left_layout.addWidget(self.file_table)

        left_layout.addWidget(self.tabs)

        #
        # Sağ Panel
        #

        right = QWidget()

        right_layout = QVBoxLayout(right)

        right_layout.addWidget(self.folder_tree)

        right_layout.addWidget(self.chart)

        #
        # Splitter
        #

        splitter = QSplitter()

        splitter.addWidget(left)

        splitter.addWidget(right)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(cards)

        layout.addWidget(splitter)

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        overview = self.service.overview()

        self.file_card.set_value(
            overview["file_count"]
        )

        self.folder_card.set_value(
            overview["folder_count"]
        )

        self.size_card.set_value(
            format_size(
                overview["total_size"]
            )
        )

        self.empty_card.set_value(
            overview["empty_folders"]
        )

        #
        # Büyük Dosyalar
        #

        self.file_table.load_files(
            self.service.largest_files()
        )

        #
        # Büyük Klasörler
        #

        self.folder_tree.load_folders(
            self.service.largest_folders()
        )

        #
        # Video
        #

        self.video_table.load_files(
            self.service.video_files()
        )

        #
        # Arşiv
        #

        self.archive_table.load_files(
            self.service.archive_files()
        )

        #
        # ISO
        #

        self.virtual_table.load_files(
            self.service.virtual_disks()
        )

        #
        # Grafik
        #

        self.chart.show_extensions(
            self.service.extension_statistics()
        )