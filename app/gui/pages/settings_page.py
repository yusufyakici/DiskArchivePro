"""
DiskArchive Pro v2
Settings Page
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QFormLayout,
    QGroupBox,
    QPushButton,
    QCheckBox,
    QSpinBox,
    QComboBox,
    QMessageBox,
)

from app.config.config import Config


class SettingsPage(QWidget):

    def __init__(self, db=None, parent=None):

        super().__init__(parent)

        self.db = db

        self.setup_ui()

        self.load_settings()

    # -------------------------------------------------
    # UI
    # -------------------------------------------------

    def setup_ui(self):

        #
        # General
        #

        self.dark_theme = QCheckBox(
            "Koyu Tema"
        )

        self.hash_files = QCheckBox(
            "Dosya Hash Hesapla"
        )

        self.follow_links = QCheckBox(
            "Sembolik Linkleri Tara"
        )

        self.enable_fts = QCheckBox(
            "FTS Aramayı Kullan"
        )

        self.thread_count = QSpinBox()

        self.thread_count.setRange(
            1,
            64,
        )

        self.max_results = QSpinBox()

        self.max_results.setRange(
            100,
            100000,
        )

        general_form = QFormLayout()

        general_form.addRow(
            self.dark_theme
        )

        general_form.addRow(
            self.hash_files
        )

        general_form.addRow(
            self.follow_links
        )

        general_form.addRow(
            self.enable_fts
        )

        general_form.addRow(
            "Thread Sayısı",
            self.thread_count,
        )

        general_form.addRow(
            "Maksimum Sonuç",
            self.max_results,
        )

        general_group = QGroupBox(
            "Genel"
        )

        general_group.setLayout(
            general_form
        )

        #
        # Database
        #

        self.vacuum_button = QPushButton(
            "VACUUM"
        )

        self.analyze_button = QPushButton(
            "ANALYZE"
        )

        self.backup_button = QPushButton(
            "Yedek Al"
        )

        db_layout = QHBoxLayout()

        db_layout.addWidget(
            self.vacuum_button
        )

        db_layout.addWidget(
            self.analyze_button
        )

        db_layout.addWidget(
            self.backup_button
        )

        database_group = QGroupBox(
            "Veritabanı"
        )

        database_group.setLayout(
            db_layout
        )

        #
        # Log
        #

        self.log_level = QComboBox()

        self.log_level.addItems(

            [

                "DEBUG",

                "INFO",

                "WARNING",

                "ERROR",

            ]

        )

        log_form = QFormLayout()

        log_form.addRow(
            "Log Seviyesi",
            self.log_level,
        )

        log_group = QGroupBox(
            "Log"
        )

        log_group.setLayout(
            log_form
        )

        #
        # Buttons
        #

        self.save_button = QPushButton(
            "Kaydet"
        )

        self.default_button = QPushButton(
            "Varsayılan"
        )

        button_layout = QHBoxLayout()

        button_layout.addStretch()

        button_layout.addWidget(
            self.default_button
        )

        button_layout.addWidget(
            self.save_button
        )

        #
        # Main
        #

        layout = QVBoxLayout(self)

        layout.addWidget(
            general_group
        )

        layout.addWidget(
            database_group
        )

        layout.addWidget(
            log_group
        )

        layout.addStretch()

        layout.addLayout(
            button_layout
        )

        #
        # Events
        #

        self.save_button.clicked.connect(
            self.save_settings
        )

        self.default_button.clicked.connect(
            self.load_defaults
        )

        self.vacuum_button.clicked.connect(
            self.database_vacuum
        )

        self.analyze_button.clicked.connect(
            self.database_analyze
        )

    # -------------------------------------------------
    # LOAD
    # -------------------------------------------------

    def load_settings(self):

        self.dark_theme.setChecked(
            Config.DEFAULT_THEME == "dark"
        )

        self.hash_files.setChecked(
            Config.HASH_FILES
        )

        self.follow_links.setChecked(
            Config.FOLLOW_SYMLINKS
        )

        self.enable_fts.setChecked(
            Config.ENABLE_FTS
        )

        self.thread_count.setValue(
            Config.THREAD_COUNT
        )

        self.max_results.setValue(
            Config.MAX_RESULTS
        )

        self.log_level.setCurrentText(
            Config.LOG_LEVEL
        )

    # -------------------------------------------------
    # SAVE
    # -------------------------------------------------

    def save_settings(self):

        #
        # İleride settings tablosuna yazılacak
        #

        QMessageBox.information(

            self,

            "Bilgi",

            "Ayarlar kaydedildi.",

        )

    # -------------------------------------------------
    # DEFAULT
    # -------------------------------------------------

    def load_defaults(self):

        self.load_settings()

    # -------------------------------------------------
    # DATABASE
    # -------------------------------------------------

    def database_vacuum(self):

        if self.db:

            self.db.vacuum()

        QMessageBox.information(

            self,

            "Bilgi",

            "VACUUM tamamlandı.",

        )

    def database_analyze(self):

        if self.db:

            self.db.analyze()

        QMessageBox.information(

            self,

            "Bilgi",

            "ANALYZE tamamlandı.",

        )