"""
DiskArchive Pro v2
Search Bar Widget
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLineEdit,
    QPushButton,
    QWidget,
)


class SearchBar(QWidget):

    # -------------------------------------------------
    # SIGNALS
    # -------------------------------------------------

    searchRequested = Signal(str)

    clearRequested = Signal()

    # -------------------------------------------------
    # INIT
    # -------------------------------------------------

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        self.search_edit = QLineEdit()

        self.search_edit.setPlaceholderText(

            "Ara... (ör: pdf, ext:pdf, size>100MB)"

        )

        self.search_button = QPushButton("🔍 Ara")

        self.clear_button = QPushButton("🗑 Temizle")

        layout = QHBoxLayout(self)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.addWidget(self.search_edit)

        layout.addWidget(self.search_button)

        layout.addWidget(self.clear_button)

        #
        # Events
        #

        self.search_button.clicked.connect(

            self.search

        )

        self.clear_button.clicked.connect(

            self.clear

        )

        self.search_edit.returnPressed.connect(

            self.search

        )

    # -------------------------------------------------
    # SEARCH
    # -------------------------------------------------

    def search(self):

        self.searchRequested.emit(

            self.search_edit.text().strip()

        )

    # -------------------------------------------------
    # CLEAR
    # -------------------------------------------------

    def clear(self):

        self.search_edit.clear()

        self.clearRequested.emit()

    # -------------------------------------------------
    # TEXT
    # -------------------------------------------------

    def text(self):

        return self.search_edit.text().strip()

    # -------------------------------------------------
    # SET TEXT
    # -------------------------------------------------

    def set_text(self, text):

        self.search_edit.setText(text)

    # -------------------------------------------------
    # FOCUS
    # -------------------------------------------------

    def focus(self):

        self.search_edit.setFocus()