"""
DiskArchive Pro v2
Folders Page
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

from app.gui.widgets.folder_tree import FolderTree
from app.gui.widgets.search_bar import SearchBar

from app.repository.folder_repository import FolderRepository
from app.utils.formatter import format_size


class FoldersPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.repository = FolderRepository(db)

        self.folders = []

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
        # Folder Tree
        #

        self.tree = FolderTree()

        #
        # Detail Panel
        #

        self.name = QLabel()

        self.path = QLabel()

        self.size = QLabel()

        self.files = QLabel()

        self.folders_label = QLabel()

        self.created = QLabel()

        self.modified = QLabel()

        form = QFormLayout()

        form.addRow("Adı :", self.name)

        form.addRow("Yolu :", self.path)

        form.addRow("Boyutu :", self.size)

        form.addRow("Dosya Sayısı :", self.files)

        form.addRow("Alt Klasör :", self.folders_label)

        form.addRow("Oluşturulma :", self.created)

        form.addRow("Değiştirilme :", self.modified)

        detail_group = QGroupBox("Klasör Bilgileri")

        detail_group.setLayout(form)

        #
        # Splitter
        #

        splitter = QSplitter(Qt.Horizontal)

        splitter.addWidget(self.tree)

        splitter.addWidget(detail_group)

        splitter.setStretchFactor(0, 2)

        splitter.setStretchFactor(1, 1)

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(top)

        layout.addWidget(splitter)

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

        self.tree.itemSelectionChanged.connect(
            self.show_details
        )

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        self.folders = self.repository.get_all()

        self.tree.load_folders(self.folders)

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self, text):

        text = text.strip()

        if not text:

            self.refresh()

            return

        self.folders = self.repository.search(text)

        self.tree.load_folders(self.folders)

    # -------------------------------------------------
    # DETAILS
    # -------------------------------------------------

    def show_details(self):

        folder_path = self.tree.current_folder()

        if not folder_path:

            return

        folder = self.repository.get_by_path(folder_path)

        if folder is None:

            return

        self.name.setText(folder.name)

        self.path.setText(folder.path)

        self.size.setText(
            format_size(folder.size)
        )

        self.files.setText(
            str(folder.file_count)
        )

        self.folders_label.setText(
            str(folder.folder_count)
        )

        self.created.setText(
            folder.created_at
        )

        self.modified.setText(
            folder.modified_at
        )