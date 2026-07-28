"""
DiskArchive Pro v2
Statistics Page
"""

from PySide6.QtWidgets import (
    QGridLayout,
    QGroupBox,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.gui.widgets.card_widget import CardWidget
from app.gui.widgets.chart_widget import ChartWidget
from app.gui.widgets.file_table import FileTable
from app.gui.widgets.folder_tree import FolderTree

from app.services.analysis_service import AnalysisService
from app.utils.formatter import format_size


class StatisticsPage(QWidget):

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
        # Cards
        #

        self.disk_card = CardWidget("Disk", "0")
        self.folder_card = CardWidget("Klasör", "0")
        self.file_card = CardWidget("Dosya", "0")
        self.size_card = CardWidget("Toplam Boyut", "0 B")

        cards = QGridLayout()

        cards.addWidget(self.disk_card, 0, 0)
        cards.addWidget(self.folder_card, 0, 1)
        cards.addWidget(self.file_card, 0, 2)
        cards.addWidget(self.size_card, 0, 3)

        #
        # Grafik
        #

        self.chart = ChartWidget()

        chart_group = QGroupBox("Dosya Türleri")

        chart_layout = QVBoxLayout()

        chart_layout.addWidget(self.chart)

        chart_group.setLayout(chart_layout)

        #
        # Uzantılar
        #

        self.extension_table = QTableWidget()

        self.extension_table.setColumnCount(3)

        self.extension_table.setHorizontalHeaderLabels(

            [

                "Uzantı",

                "Dosya",

                "Boyut",

            ]

        )

        ext_group = QGroupBox("Dosya Türleri")

        ext_layout = QVBoxLayout()

        ext_layout.addWidget(self.extension_table)

        ext_group.setLayout(ext_layout)

        #
        # Büyük Dosyalar
        #

        self.file_table = FileTable()

        file_group = QGroupBox(

            "En Büyük Dosyalar"

        )

        file_layout = QVBoxLayout()

        file_layout.addWidget(

            self.file_table

        )

        file_group.setLayout(file_layout)

        #
        # Büyük Klasörler
        #

        self.folder_tree = FolderTree()

        folder_group = QGroupBox(

            "En Büyük Klasörler"

        )

        folder_layout = QVBoxLayout()

        folder_layout.addWidget(

            self.folder_tree

        )

        folder_group.setLayout(folder_layout)

        #
        # Splitter
        #

        splitter = QSplitter()

        splitter.addWidget(file_group)

        splitter.addWidget(folder_group)

        splitter.setStretchFactor(0, 1)
        splitter.setStretchFactor(1, 1)

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(cards)

        layout.addWidget(chart_group)

        layout.addWidget(ext_group)

        layout.addWidget(splitter)

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        overview = self.service.overview()

        self.disk_card.set_value(
            overview["disk_count"]
        )

        self.folder_card.set_value(
            overview["folder_count"]
        )

        self.file_card.set_value(
            overview["file_count"]
        )

        self.size_card.set_value(
            format_size(
                overview["total_size"]
            )
        )

        #
        # Grafik
        #

        rows = self.service.extension_statistics()

        self.chart.show_extensions(rows)

        #
        # Uzantılar
        #

        self.extension_table.setRowCount(len(rows))

        for row_index, row in enumerate(rows):

            self.extension_table.setItem(
                row_index,
                0,
                QTableWidgetItem(
                    row["extension"]
                ),
            )

            self.extension_table.setItem(
                row_index,
                1,
                QTableWidgetItem(
                    str(row["file_count"])
                ),
            )

            self.extension_table.setItem(
                row_index,
                2,
                QTableWidgetItem(
                    format_size(
                        row["total_size"] or 0
                    )
                ),
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