"""
DiskArchive Pro v2
Card Widget
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class CardWidget(QFrame):

    def __init__(
        self,
        title="",
        value="",
        parent=None,
    ):

        super().__init__(parent)

        self.title = QLabel(title)

        self.value = QLabel(str(value))

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        self.setFrameShape(QFrame.StyledPanel)

        self.setObjectName("CardWidget")

        self.setMinimumHeight(120)

        layout = QVBoxLayout(self)

        #
        # Title
        #

        self.title.setAlignment(
            Qt.AlignCenter
        )

        self.title.setObjectName(
            "CardTitle"
        )

        #
        # Value
        #

        self.value.setAlignment(
            Qt.AlignCenter
        )

        self.value.setObjectName(
            "CardValue"
        )

        layout.addStretch()

        layout.addWidget(self.title)

        layout.addWidget(self.value)

        layout.addStretch()

    # -------------------------------------------------
    # SET VALUE
    # -------------------------------------------------

    def set_value(self, value):

        self.value.setText(str(value))

    # -------------------------------------------------
    # SET TITLE
    # -------------------------------------------------

    def set_title(self, title):

        self.title.setText(title)