"""
DiskArchive Pro v2
Progress Widget
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
    QProgressBar,
)

from app.utils.formatter import (
    format_number,
    format_size,
)


class ProgressWidget(QWidget):

    def __init__(self, parent=None):

        super().__init__(parent)

        self.build_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def build_ui(self):

        #
        # Progress
        #

        self.progress = QProgressBar()

        self.progress.setMinimum(0)

        self.progress.setMaximum(100)

        self.progress.setValue(0)

        #
        # Labels
        #

        self.status_label = QLabel("Hazır")

        self.files_label = QLabel("Dosya : 0")

        self.folders_label = QLabel("Klasör : 0")

        self.size_label = QLabel("Boyut : 0 B")

        #
        # Info Layout
        #

        info = QHBoxLayout()

        info.addWidget(self.files_label)

        info.addSpacing(20)

        info.addWidget(self.folders_label)

        info.addSpacing(20)

        info.addWidget(self.size_label)

        info.addStretch()

        #
        # Main
        #

        layout = QVBoxLayout(self)

        layout.addWidget(self.status_label)

        layout.addWidget(self.progress)

        layout.addLayout(info)
            # -------------------------------------------------
    # STATUS
    # -------------------------------------------------

    def set_status(self, text):

        self.status_label.setText(text)

    # -------------------------------------------------
    # PROGRESS
    # -------------------------------------------------

    def set_progress(self, value):

        self.progress.setValue(value)
        # -------------------------------------------------
    # PROGRESS
    # -------------------------------------------------

    def set_progress(self, value):

        self.progress.setValue(value)

    # -------------------------------------------------
    # QT COMPATIBILITY
    # -------------------------------------------------

    def setValue(self, value):

        self.progress.setValue(value)

    def value(self):

        return self.progress.value()

    def setMaximum(self, value):

        self.progress.setMaximum(value)

    def maximum(self):

        return self.progress.maximum()

    def setMinimum(self, value):

        self.progress.setMinimum(value)

    def minimum(self):

        return self.progress.minimum()

    # -------------------------------------------------
    # FILES
    # -------------------------------------------------

    def set_files(self, count):

        self.files_label.setText(

            f"Dosya : {format_number(count)}"

        )

    # -------------------------------------------------
    # FOLDERS
    # -------------------------------------------------

    def set_folders(self, count):

        self.folders_label.setText(

            f"Klasör : {format_number(count)}"

        )

    # -------------------------------------------------
    # SIZE
    # -------------------------------------------------

    def set_size(self, size):

        self.size_label.setText(

            f"Boyut : {format_size(size)}"

        )

    # -------------------------------------------------
    # RESET
    # -------------------------------------------------

    def reset(self):

        self.progress.setValue(0)

        self.status_label.setText("Hazır")

        self.files_label.setText("Dosya : 0")

        self.folders_label.setText("Klasör : 0")

        self.size_label.setText("Boyut : 0 B")
