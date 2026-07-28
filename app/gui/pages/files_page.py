"""
DiskArchive Pro v2
Files Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
    QVBoxLayout,
    QWidget,
)

from app.gui.widgets.file_table import FileTable
from app.gui.widgets.search_bar import SearchBar
from app.gui.widgets.status_widget import StatusWidget

from app.repository.file_repository import FileRepository
from app.utils.formatter import format_size


class FilesPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.repository = FileRepository(db)

        self.files = []

        self.setup_ui()

        self.refresh()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Search
        #

        self.search_bar = SearchBar()

        self.refresh_button = QPushButton("🔄 Yenile")

        top = QHBoxLayout()

        top.addWidget(self.search_bar)

        top.addWidget(self.refresh_button)

        #
        # Table
        #

        self.table = FileTable()

        #
        # Detail Panel
        #

        self.name = QLabel()

        self.extension = QLabel()

        self.path = QLabel()

        self.size = QLabel()

        self.created = QLabel()

        self.modified = QLabel()

        form = QFormLayout()

        form.addRow("Dosya :", self.name)

        form.addRow("Uzantı :", self.extension)

        form.addRow("Tam Yol :", self.path)

        form.addRow("Boyut :", self.size)

        form.addRow("Oluşturulma :", self.created)

        form.addRow("Değiştirilme :", self.modified)

        detail_group = QGroupBox(
            "Dosya Bilgileri"
        )

        detail_group.setLayout(form)

        #
        # Splitter
        #

        splitter = QSplitter(Qt.Vertical)

        splitter.addWidget(self.table)

        splitter.addWidget(detail_group)

        splitter.setStretchFactor(0, 3)

        splitter.setStretchFactor(1, 1)

        #
        # Status
        #

        self.status = StatusWidget()

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(top)

        layout.addWidget(splitter)

        layout.addWidget(self.status)

        #
        # Events
        #

        self.refresh_button.clicked.connect(
            self.refresh
        )

        self.search_bar.searchRequested.connect(
            self.search
        )

        self.search_bar.clearRequested.connect(
            self.refresh
        )

        self.table.itemSelectionChanged.connect(
            self.show_details
        )

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        self.files = self.repository.get_all()

        self.table.load_files(self.files)

        self.status.set_file_count(
            len(self.files)
        )

        self.status.set_total_size(
            self.repository.total_size()
        )

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self, text):

        filters = {

            "name": text,

            "extension": None,

            "min_size": None,

            "max_size": None,

            "date": None,

        }

        self.files = self.repository.search(filters)

        self.table.load_files(self.files)

        self.status.set_file_count(
            len(self.files)
        )

    # -------------------------------------------------
    # DETAILS
    # -------------------------------------------------

    def show_details(self):

        row = self.table.currentRow()

        if row < 0:

            return

        if row >= len(self.files):

            return

        file = self.files[row]

        self.name.setText(file.name)

        self.extension.setText(file.extension)

        self.path.setText(file.full_path)

        self.size.setText(
            format_size(file.size)
        )

        self.created.setText(
            file.created_at
        )

        self.modified.setText(
            file.modified_at
        )

        self.status.set_selected(1)