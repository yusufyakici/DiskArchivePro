"""
DiskArchive Pro v2
Reports Page
"""

from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QCheckBox,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from app.config.config import Config


class ReportsPage(QWidget):

    def __init__(self, db, parent=None):

        super().__init__(parent)

        self.db = db

        self.setup_ui()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # Format
        #

        self.pdf = QCheckBox("PDF")

        self.excel = QCheckBox("Excel")

        self.csv = QCheckBox("CSV")

        self.html = QCheckBox("HTML")

        self.pdf.setChecked(True)

        format_group = QGroupBox("Rapor Formatı")

        format_layout = QVBoxLayout()

        format_layout.addWidget(self.pdf)
        format_layout.addWidget(self.excel)
        format_layout.addWidget(self.csv)
        format_layout.addWidget(self.html)

        format_group.setLayout(format_layout)

        #
        # İçerik
        #

        self.disk = QCheckBox("Disk Bilgileri")
        self.folder = QCheckBox("Klasörler")
        self.file = QCheckBox("Dosyalar")
        self.largest_file = QCheckBox("En Büyük Dosyalar")
        self.largest_folder = QCheckBox("En Büyük Klasörler")
        self.extension = QCheckBox("Uzantı İstatistikleri")

        for checkbox in (
            self.disk,
            self.folder,
            self.file,
            self.largest_file,
            self.largest_folder,
            self.extension,
        ):
            checkbox.setChecked(True)

        content_group = QGroupBox("Rapor İçeriği")

        content_layout = QVBoxLayout()

        content_layout.addWidget(self.disk)
        content_layout.addWidget(self.folder)
        content_layout.addWidget(self.file)
        content_layout.addWidget(self.largest_file)
        content_layout.addWidget(self.largest_folder)
        content_layout.addWidget(self.extension)

        content_group.setLayout(content_layout)

        #
        # Log
        #

        self.log = QTextEdit()

        self.log.setReadOnly(True)

        #
        # Buttons
        #

        self.generate_button = QPushButton(
            "📄 Rapor Oluştur"
        )

        self.open_button = QPushButton(
            "📂 Export Klasörünü Aç"
        )

        buttons = QHBoxLayout()

        buttons.addWidget(self.generate_button)
        buttons.addWidget(self.open_button)
        buttons.addStretch()

        #
        # Main Layout
        #

        layout = QVBoxLayout(self)

        layout.addWidget(format_group)
        layout.addWidget(content_group)
        layout.addWidget(QLabel("İşlem Günlüğü"))
        layout.addWidget(self.log)
        layout.addLayout(buttons)

        #
        # Events
        #

        self.generate_button.clicked.connect(
            self.generate_reports
        )

        self.open_button.clicked.connect(
            self.open_export_folder
        )

    # -------------------------------------------------
    # GENERATE
    # -------------------------------------------------

    def generate_reports(self):

        self.log.clear()

        if self.pdf.isChecked():

            self.log.append("✓ PDF raporu oluşturulacak.")

        if self.excel.isChecked():

            self.log.append("✓ Excel raporu oluşturulacak.")

        if self.csv.isChecked():

            self.log.append("✓ CSV raporu oluşturulacak.")

        if self.html.isChecked():

            self.log.append("✓ HTML raporu oluşturulacak.")

        self.log.append("")
        self.log.append("Rapor oluşturma işlemi başlatıldı.")

        #
        # Burada ReportService çağrılacak
        #

        QMessageBox.information(

            self,

            "Bilgi",

            "Rapor oluşturma modülü henüz bağlanmadı.",

        )

    # -------------------------------------------------
    # OPEN EXPORT
    # -------------------------------------------------

    def open_export_folder(self):

        export_dir = Path(Config.EXPORT_DIR)

        QFileDialog.getOpenFileName(
            self,
            "Export Klasörü",
            str(export_dir),
        )