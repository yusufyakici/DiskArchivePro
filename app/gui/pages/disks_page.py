"""
DiskArchive Pro v2
Disks Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSplitter,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)

from app.repository.disk_repository import DiskRepository
from app.utils.formatter import format_size


class DisksPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.repository = DiskRepository(db)

        self.setup_ui()

        self.refresh()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Buttons
        #

        self.scan_button = QPushButton("💽 Tara")

        self.refresh_button = QPushButton("🔄 Yenile")

        self.delete_button = QPushButton("🗑 Sil")

        button_layout = QHBoxLayout()

        button_layout.addWidget(self.scan_button)

        button_layout.addWidget(self.refresh_button)

        button_layout.addWidget(self.delete_button)

        button_layout.addStretch()

        #
        # Disk Table
        #

        self.table = QTableWidget()

        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels(

            [

                "Sürücü",

                "Etiket",

                "Dosya Sistemi",

                "Toplam",

                "Boş",

                "Kullanım",

            ]

        )

        #
        # Detail Panel
        #

        self.drive = QLabel()

        self.label = QLabel()

        self.serial = QLabel()

        self.filesystem = QLabel()

        self.capacity = QLabel()

        self.used = QLabel()

        self.free = QLabel()

        form = QFormLayout()

        form.addRow("Sürücü :", self.drive)

        form.addRow("Etiket :", self.label)

        form.addRow("Seri No :", self.serial)

        form.addRow("Dosya Sistemi :", self.filesystem)

        form.addRow("Toplam :", self.capacity)

        form.addRow("Kullanılan :", self.used)

        form.addRow("Boş :", self.free)

        detail_group = QGroupBox(

            "Disk Bilgileri"

        )

        detail_group.setLayout(form)

        #
        # Splitter
        #

        splitter = QSplitter(Qt.Vertical)

        splitter.addWidget(self.table)

        splitter.addWidget(detail_group)

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addLayout(button_layout)

        layout.addWidget(splitter)

        #
        # Events
        #

        self.table.itemSelectionChanged.connect(

            self.show_details

        )

        self.refresh_button.clicked.connect(

            self.refresh

        )

    # -------------------------------------------------
    # REFRESH
    # -------------------------------------------------

    def refresh(self):

        disks = self.repository.get_all()

        self.table.setRowCount(len(disks))

        for row, disk in enumerate(disks):

            self.table.setItem(

                row,

                0,

                QTableWidgetItem(

                    disk.drive_letter

                ),

            )

            self.table.setItem(

                row,

                1,

                QTableWidgetItem(

                    disk.label

                ),

            )

            self.table.setItem(

                row,

                2,

                QTableWidgetItem(

                    disk.file_system

                ),

            )

            self.table.setItem(

                row,

                3,

                QTableWidgetItem(

                    format_size(

                        disk.capacity

                    )

                ),

            )

            self.table.setItem(

                row,

                4,

                QTableWidgetItem(

                    format_size(

                        disk.free_space

                    )

                ),

            )

            self.table.setItem(

                row,

                5,

                QTableWidgetItem(

                    f"%{disk.used_percent}"

                ),

            )

        if disks:

            self.table.selectRow(0)

    # -------------------------------------------------
    # DETAILS
    # -------------------------------------------------

    def show_details(self):

        row = self.table.currentRow()

        if row < 0:

            return

        disk = self.repository.get_all()[row]

        self.drive.setText(disk.drive_letter)

        self.label.setText(disk.label)

        self.serial.setText(disk.serial_number)

        self.filesystem.setText(disk.file_system)

        self.capacity.setText(

            format_size(

                disk.capacity

            )

        )

        self.used.setText(

            format_size(

                disk.used_space

            )

        )

        self.free.setText(

            format_size(

                disk.free_space

            )

        )