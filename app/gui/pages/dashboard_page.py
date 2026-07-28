"""
DiskArchive Pro v2
Dashboard Page
"""

from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from app.gui.widgets.card_widget import CardWidget
from app.gui.widgets.chart_widget import ChartWidget
from app.gui.widgets.file_table import FileTable
from app.gui.widgets.folder_tree import FolderTree

from app.services.dashboard_service import DashboardService


class DashboardPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.service = DashboardService(db)

        self.setup_ui()

        self.refresh()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Kartlar
        #

        self.disk_card = CardWidget(
            "Disk",
            "0",
        )

        self.folder_card = CardWidget(
            "Klasör",
            "0",
        )

        self.file_card = CardWidget(
            "Dosya",
            "0",
        )

        self.size_card = CardWidget(
            "Toplam Boyut",
            "0 B",
        )

        self.empty_folder_card = CardWidget(
            "Boş Klasör",
            "0",
        )

        self.empty_file_card = CardWidget(
            "Boş Dosya",
            "0",
        )

        card_layout = QGridLayout()

        card_layout.addWidget(
            self.disk_card,
            0,
            0,
        )

        card_layout.addWidget(
            self.folder_card,
            0,
            1,
        )

        card_layout.addWidget(
            self.file_card,
            0,
            2,
        )

        card_layout.addWidget(
            self.size_card,
            1,
            0,
        )

        card_layout.addWidget(
            self.empty_folder_card,
            1,
            1,
        )

        card_layout.addWidget(
            self.empty_file_card,
            1,
            2,
        )

        #
        # Grafik
        #

        self.chart = ChartWidget()

        chart_group = QGroupBox(
            "Dosya Türleri"
        )

        chart_layout = QVBoxLayout()

        chart_layout.addWidget(
            self.chart
        )

        chart_group.setLayout(
            chart_layout
        )

        #
        # En Büyük Dosyalar
        #

        self.file_table = FileTable()

        file_group = QGroupBox(
            "En Büyük Dosyalar"
        )

        file_layout = QVBoxLayout()

        file_layout.addWidget(
            self.file_table
        )

        file_group.setLayout(
            file_layout
        )

        #
        # En Büyük Klasörler
        #

        self.folder_tree = FolderTree()

        folder_group = QGroupBox(
            "En Büyük Klasörler"
        )

        folder_layout = QVBoxLayout()

        folder_layout.addWidget(
            self.folder_tree
        )

        folder_group.setLayout(
            folder_layout
        )

        #
        # Alt Bölüm
        #

        splitter = QSplitter()

        splitter.addWidget(
            file_group
        )

        splitter.addWidget(
            folder_group
        )

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)

        #
        # Ana Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(card_layout)

        layout.addWidget(chart_group)

        layout.addWidget(splitter)

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        stats = self.service.get_statistics()

        self.disk_card.set_value(
            stats["disk_count"]
        )

        self.folder_card.set_value(
            stats["folder_count"]
        )

        self.file_card.set_value(
            stats["file_count"]
        )

        self.size_card.set_value(
            self.format_size(
                stats["total_file_size"]
            )
        )

        self.empty_folder_card.set_value(
            self.service.get_empty_folder_count()
        )

        self.empty_file_card.set_value(
            self.service.get_empty_file_count()
        )

        #
        # Büyük Dosyalar
        #

        self.file_table.load_files(

            self.service.get_largest_files()

        )

        #
        # Büyük Klasörler
        #

        self.folder_tree.load_folders(

            self.service.get_largest_folders()

        )

        #
        # Grafik
        #

        self.chart.show_extensions(

            self.service.get_extension_statistics()

        )

    # -------------------------------------------------
    # FORMAT SIZE
    # -------------------------------------------------

    @staticmethod
    def format_size(size):

        size = float(size)

        units = [
            "B",
            "KB",
            "MB",
            "GB",
            "TB",
            "PB",
        ]

        for unit in units:

            if size < 1024:

                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} PB"