"""
DiskArchive Pro v2
File Table Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
)


class FileTable(QTableWidget):

    HEADERS = [

        "Dosya Adı",

        "Uzantı",

        "Boyut",

        "Klasör",

        "Oluşturulma",

        "Değiştirilme",

    ]

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        self.setColumnCount(

            len(self.HEADERS)

        )

        self.setHorizontalHeaderLabels(

            self.HEADERS

        )

        self.setSelectionBehavior(

            QAbstractItemView.SelectRows

        )

        self.setSelectionMode(

            QAbstractItemView.SingleSelection

        )

        self.setEditTriggers(

            QAbstractItemView.NoEditTriggers

        )

        self.setAlternatingRowColors(True)

        self.setSortingEnabled(True)

        self.verticalHeader().hide()

        header = self.horizontalHeader()

        header.setStretchLastSection(True)

        header.setSectionResizeMode(

            0,

            QHeaderView.Stretch,

        )

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear_files(self):

        self.setRowCount(0)

    # -------------------------------------------------
    # LOAD
    # -------------------------------------------------

    def load_files(self, files):

        self.setSortingEnabled(False)

        self.setRowCount(0)

        for file in files:

            self.add_file(file)

        self.setSortingEnabled(True)

    # -------------------------------------------------
    # ADD
    # -------------------------------------------------

    def add_file(self, file):

        row = self.rowCount()

        self.insertRow(row)

        self.setItem(

            row,

            0,

            QTableWidgetItem(file.name),

        )

        self.setItem(

            row,

            1,

            QTableWidgetItem(file.extension),

        )

        self.setItem(

            row,

            2,

            QTableWidgetItem(

                file.formatted_size

            ),

        )

        self.setItem(

            row,

            3,

            QTableWidgetItem(

                file.directory

            ),

        )

        self.setItem(

            row,

            4,

            QTableWidgetItem(

                file.created_at

            ),

        )

        self.setItem(

            row,

            5,

            QTableWidgetItem(

                file.modified_at

            ),

        )

    # -------------------------------------------------
    # CURRENT FILE
    # -------------------------------------------------

    def current_file_name(self):

        row = self.currentRow()

        if row < 0:

            return None

        item = self.item(row, 0)

        if item:

            return item.text()

        return None