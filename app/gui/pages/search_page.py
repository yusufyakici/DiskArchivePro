"""
DiskArchive Pro v2
Search Page
"""

from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

from app.gui.widgets.file_table import FileTable
from app.gui.widgets.search_bar import SearchBar
from app.gui.widgets.status_widget import StatusWidget

from app.services.search_service import SearchService


class SearchPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.service = SearchService(db)

        self.files = []

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Search
        #

        self.search_bar = SearchBar()

        self.refresh_button = QPushButton("Temizle")

        top = QHBoxLayout()

        top.addWidget(self.search_bar)

        top.addWidget(self.refresh_button)

        #
        # Result
        #

        self.result_label = QLabel(
            "Sonuç : 0 dosya"
        )

        #
        # Table
        #

        self.table = FileTable()

        #
        # Status
        #

        self.status = StatusWidget()

        #
        # Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(top)

        layout.addWidget(self.result_label)

        layout.addWidget(self.table)

        layout.addWidget(self.status)

        #
        # Events
        #

        self.search_bar.searchRequested.connect(
            self.search
        )

        self.search_bar.clearRequested.connect(
            self.clear
        )

        self.refresh_button.clicked.connect(
            self.clear
        )

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self, text):

        result = self.service.search(text)

        self.files = result["files"]

        self.table.load_files(
            self.files
        )

        self.result_label.setText(

            f"Sonuç : {len(self.files):,} dosya"

        )

        self.status.set_file_count(

            len(self.files)

        )

        total = sum(

            file.size

            for file in self.files

        )

        self.status.set_total_size(total)

        self.status.set_status(
            "Arama tamamlandı."
        )

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear(self):

        self.files.clear()

        self.table.clear_files()

        self.result_label.setText(
            "Sonuç : 0 dosya"
        )

        self.status.reset()