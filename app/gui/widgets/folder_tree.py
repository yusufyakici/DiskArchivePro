"""
DiskArchive Pro v2
Folder Tree Widget
"""

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTreeWidget,
    QTreeWidgetItem,
)


class FolderTree(QTreeWidget):

    HEADERS = [

        "Klasör",

        "Boyut",

        "Dosya",

        "Alt Klasör",

    ]

    def __init__(self, parent=None):

        super().__init__(parent)

        self.items = {}

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        self.setColumnCount(
            len(self.HEADERS)
        )

        self.setHeaderLabels(
            self.HEADERS
        )

        self.setAlternatingRowColors(True)

        self.setSelectionBehavior(
            QAbstractItemView.SelectRows
        )

        self.setSelectionMode(
            QAbstractItemView.SingleSelection
        )

        self.setAnimated(True)

        self.setUniformRowHeights(True)

        self.header().setSectionResizeMode(
            0,
            QHeaderView.Stretch,
        )

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear_tree(self):

        self.items.clear()

        self.clear()

    # -------------------------------------------------
    # LOAD
    # -------------------------------------------------

    def load_folders(self, folders):

        self.clear_tree()

        #
        # Derinliğe göre sırala
        #

        folders = sorted(

            folders,

            key=lambda f: len(
                Path(f.path).parts
            ),

        )

        for folder in folders:

            self.add_folder(folder)

        self.expandToDepth(1)

    # -------------------------------------------------
    # ADD
    # -------------------------------------------------

    def add_folder(self, folder):

        item = QTreeWidgetItem(

            [

                folder.name,

                self.format_size(folder.size),

                str(folder.file_count),

                str(folder.folder_count),

            ]

        )

        self.items[folder.path] = item

        #
        # Parent
        #

        parent_path = str(

            Path(folder.path).parent

        )

        parent = self.items.get(
            parent_path
        )

        if parent:

            parent.addChild(item)

        else:

            self.addTopLevelItem(item)

    # -------------------------------------------------
    # CURRENT PATH
    # -------------------------------------------------

    def current_folder(self):

        item = self.currentItem()

        if item:

            return item.text(0)

        return None

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

        ]

        for unit in units:

            if size < 1024:

                return f"{size:.2f} {unit}"

            size /= 1024

        return f"{size:.2f} PB"