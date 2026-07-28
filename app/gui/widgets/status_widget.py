"""
DiskArchive Pro v2
Status Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
)


class StatusWidget(QFrame):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        self.setObjectName("StatusWidget")

        #
        # Durum
        #

        self.status_label = QLabel("Hazır")

        #
        # Seçili
        #

        self.selected_label = QLabel(
            "Seçili : 0"
        )

        #
        # Dosya
        #

        self.file_label = QLabel(
            "Dosya : 0"
        )

        #
        # Klasör
        #

        self.folder_label = QLabel(
            "Klasör : 0"
        )

        #
        # Toplam Boyut
        #

        self.size_label = QLabel(
            "Boyut : 0 B"
        )

        #
        # Layout
        #

        layout = QHBoxLayout(self)

        layout.setContentsMargins(
            8,
            4,
            8,
            4,
        )

        layout.addWidget(self.status_label)

        layout.addStretch()

        layout.addWidget(self.selected_label)

        layout.addSpacing(15)

        layout.addWidget(self.file_label)

        layout.addSpacing(15)

        layout.addWidget(self.folder_label)

        layout.addSpacing(15)

        layout.addWidget(self.size_label)

    # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    def set_status(self, text):

        self.status_label.setText(text)

    # -------------------------------------------------
    # SELECTED
    # -------------------------------------------------

    def set_selected(self, count):

        self.selected_label.setText(
            f"Seçili : {count:,}"
        )

    # -------------------------------------------------
    # FILE COUNT
    # -------------------------------------------------

    def set_file_count(self, count):

        self.file_label.setText(
            f"Dosya : {count:,}"
        )

    # -------------------------------------------------
    # FOLDER COUNT
    # -------------------------------------------------

    def set_folder_count(self, count):

        self.folder_label.setText(
            f"Klasör : {count:,}"
        )

    # -------------------------------------------------
    # TOTAL SIZE
    # -------------------------------------------------

    def set_total_size(self, size):

        self.size_label.setText(
            f"Boyut : {self.format_size(size)}"
        )

    # -------------------------------------------------
    # RESET
    # -------------------------------------------------

    def reset(self):

        self.set_status("Hazır")

        self.set_selected(0)

        self.set_file_count(0)

        self.set_folder_count(0)

        self.set_total_size(0)

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