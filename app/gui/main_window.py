"""
DiskArchive Pro v2
Main Window
"""

from PySide6.QtCore import Qt, QThread

from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QFileDialog,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QToolBar,
)

from app.config.config import Config
from app.database.database import Database

from app.workers.scan_worker import ScanWorker

from app.services.disk_service import DiskService
from app.services.dashboard_service import DashboardService
from app.services.search_service import SearchService

from app.gui.widgets.status_widget import StatusWidget
from app.gui.widgets.progress_widget import ProgressWidget

from app.gui.pages.dashboard_page import DashboardPage
from app.gui.pages.disks_page import DisksPage
from app.gui.pages.folders_page import FoldersPage
from app.gui.pages.files_page import FilesPage
from app.gui.pages.search_page import SearchPage
from app.gui.pages.analysis_page import AnalysisPage
from app.gui.pages.statistics_page import StatisticsPage
from app.gui.pages.reports_page import ReportsPage
from app.gui.pages.settings_page import SettingsPage

from app.utils.logger import Logger


class MainWindow(QMainWindow):

    # -------------------------------------------------
    # INIT
    # -------------------------------------------------

    def __init__(self, db: Database):

        super().__init__()

        #
        # Database
        #

        self.db = db

        #
        # Services
        #

        self.disk_service = DiskService(db)

        self.dashboard_service = DashboardService(db)

        self.search_service = SearchService(db)

        #
        # Thread
        #

        self.thread = None

        self.worker = None

        #
        # Window
        #

        self.setup_window()

        #
        # UI
        #

        self.build_ui()

        Logger.info(
            "MainWindow oluşturuldu."
        )

    # -------------------------------------------------
    # WINDOW
    # -------------------------------------------------

    def setup_window(self):

        self.setWindowTitle(
            Config.WINDOW_TITLE
        )

        self.resize(

            Config.WINDOW_WIDTH,

            Config.WINDOW_HEIGHT,

        )

        self.setMinimumSize(

            1200,

            800,

        )

    # -------------------------------------------------
    # BUILD UI
    # -------------------------------------------------

    def build_ui(self):

        #
        # Oluştur
        #

        self.create_toolbar()

        self.create_menu()

        self.create_pages()

        self.create_statusbar()

        #
        # Splitter
        #

        splitter = QSplitter(
            Qt.Orientation.Horizontal
        )

        splitter.addWidget(
            self.menu
        )

        splitter.addWidget(
            self.pages
        )

        splitter.setStretchFactor(
            0,
            0,
        )

        splitter.setStretchFactor(
            1,
            1,
        )

        self.setCentralWidget(
            splitter
        )

        #
        # Signal
        #

        self.connect_signals()

        #
        # İlk Sayfa
        #

        self.menu.setCurrentRow(0)

    # -------------------------------------------------
    # TOOLBAR
    # -------------------------------------------------

    def create_toolbar(self):

        toolbar = QToolBar(
            "Ana Araç Çubuğu"
        )

        toolbar.setMovable(False)

        self.addToolBar(toolbar)

        #
        # Actions
        #

        self.scan_action = QAction(
            "💽 Disk Tara",
            self,
        )

        self.refresh_action = QAction(
            "🔄 Yenile",
            self,
        )

        self.report_action = QAction(
            "📄 Raporlar",
            self,
        )

        self.settings_action = QAction(
            "⚙ Ayarlar",
            self,
        )

        toolbar.addAction(
            self.scan_action
        )

        toolbar.addSeparator()

        toolbar.addAction(
            self.refresh_action
        )

        toolbar.addSeparator()

        toolbar.addAction(
            self.report_action
        )

        toolbar.addSeparator()

        toolbar.addAction(
            self.settings_action
        )

    # -------------------------------------------------
    # MENU
    # -------------------------------------------------

    def create_menu(self):

        self.menu = QListWidget()

        self.menu.setMaximumWidth(220)

        self.menu.setMinimumWidth(220)

        pages = [

            "🏠 Dashboard",

            "💽 Diskler",

            "📁 Klasörler",

            "📄 Dosyalar",

            "🔍 Arama",

            "📊 Analiz",

            "📈 İstatistikler",

            "📝 Raporlar",

            "⚙ Ayarlar",

        ]

        for page in pages:

            QListWidgetItem(

                page,

                self.menu,

            )

    # -------------------------------------------------
    # PAGES
    # -------------------------------------------------

    def create_pages(self):

        self.pages = QStackedWidget()

        #
        # Pages
        #

        self.dashboard_page = DashboardPage(
            self.db
        )

        self.disks_page = DisksPage(
            self.db
        )

        self.folders_page = FoldersPage(
            self.db
        )

        self.files_page = FilesPage(
            self.db
        )

        self.search_page = SearchPage(
            self.db
        )

        self.analysis_page = AnalysisPage(
            self.db
        )

        self.statistics_page = StatisticsPage(
            self.db
        )

        self.reports_page = ReportsPage(
            self.db
        )

        self.settings_page = SettingsPage(
            self.db
        )

        #
        # Add Pages
        #

        self.pages.addWidget(
            self.dashboard_page
        )

        self.pages.addWidget(
            self.disks_page
        )

        self.pages.addWidget(
            self.folders_page
        )

        self.pages.addWidget(
            self.files_page
        )

        self.pages.addWidget(
            self.search_page
        )

        self.pages.addWidget(
            self.analysis_page
        )

        self.pages.addWidget(
            self.statistics_page
        )

        self.pages.addWidget(
            self.reports_page
        )

        self.pages.addWidget(
            self.settings_page
        )

    # -------------------------------------------------
    # STATUS BAR
    # -------------------------------------------------

    def create_statusbar(self):

        self.status_widget = StatusWidget()

        self.progress_widget = ProgressWidget()

        statusbar = QStatusBar()

        statusbar.addWidget(

            self.status_widget,

            1,

        )

        statusbar.addPermanentWidget(

            self.progress_widget,

        )

        self.setStatusBar(

            statusbar

        )

    # -------------------------------------------------
    # CONNECT SIGNALS
    # -------------------------------------------------

    def connect_signals(self):

        #
        # Sol Menü
        #

        self.menu.currentRowChanged.connect(
            self.change_page
        )

        #
        # Toolbar
        #

        self.scan_action.triggered.connect(
            self.scan_disk
        )

        self.refresh_action.triggered.connect(
            self.refresh_pages
        )

        self.report_action.triggered.connect(

            lambda: self.change_page(7)

        )

        self.settings_action.triggered.connect(

            lambda: self.change_page(8)

        )

    # -------------------------------------------------
    # CHANGE PAGE
    # -------------------------------------------------

    def change_page(self, index):

        self.pages.setCurrentIndex(index)

        page_name = self.menu.item(index).text()

        self.status_widget.set_status(
            f"Açıldı : {page_name}"
        )

    # -------------------------------------------------
    # REFRESH PAGES
    # -------------------------------------------------

    def refresh_pages(self):

        refresh_methods = [

            ("Dashboard", self.dashboard_page),

            ("Diskler", self.disks_page),

            ("Klasörler", self.folders_page),

            ("Dosyalar", self.files_page),

            ("Analiz", self.analysis_page),

            ("İstatistik", self.statistics_page),

        ]

        for name, page in refresh_methods:

            if hasattr(page, "refresh"):

                try:

                    page.refresh()

                except Exception as e:

                    Logger.exception(
                        f"{name} yenilenemedi : {e}"
                    )

        self.status_widget.set_status(
            "Sayfalar güncellendi."
        )
    # -------------------------------------------------
    # SCAN DISK
    # -------------------------------------------------

    def scan_disk(self):

        path = QFileDialog.getExistingDirectory(

            self,

            "Taranacak Klasörü Seç",

        )

        if not path:

            return

        Logger.info(
            f"Seçilen klasör : {path}"
        )

        self.start_scan(path)

    # -------------------------------------------------
    # START SCAN
    # -------------------------------------------------

    def start_scan(self, path):

        #
        # Worker çalışıyor mu?
        #

        if self.worker is not None:

            QMessageBox.warning(

                self,

                "Tarama",

                "Zaten çalışan bir tarama var.",

            )

            return

        #
        # Toolbar
        #

        self.scan_action.setEnabled(False)

        self.refresh_action.setEnabled(False)

        #
        # Status
        #

        self.status_widget.set_status(
            "Tarama hazırlanıyor..."
        )

        self.progress_widget.set_progress(0)

        #
        # Thread
        #

        self.thread = QThread()

        #
        # Worker
        #

        self.worker = ScanWorker(

            self.db,

            path,

        )

        #
        # Thread'e taşı
        #

        self.worker.moveToThread(
            self.thread
        )

        #
        # Thread Başlayınca
        #

        self.thread.started.connect(
            self.worker.run
        )

        #
        # Worker Signals
        #

        self.worker.started.connect(

            lambda: self.status_widget.set_status(
                "Tarama başladı..."
            )

        )

        self.worker.progress.connect(
            self.scan_progress
        )

        self.worker.status.connect(
            self.scan_status
        )

        self.worker.finished.connect(
            self.scan_finished
        )

        self.worker.error.connect(
            self.scan_error
        )

        #
        # Thread Cleanup
        #

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.finished.connect(
            self.scan_thread_finished
        )

        #
        # Başlat
        #

        self.thread.start()
    # -------------------------------------------------
    # SCAN PROGRESS
    # -------------------------------------------------

    def scan_progress(self, value):

        #
        # Progress Widget
        #

        self.progress_widget.set_progress(value)

    # -------------------------------------------------
    # SCAN STATUS
    # -------------------------------------------------

    def scan_status(self, text):

        self.status_widget.set_status(text)

    # -------------------------------------------------
    # SCAN FINISHED
    # -------------------------------------------------

    def scan_finished(self, statistics):

        Logger.info(
            "Tarama başarıyla tamamlandı."
        )

        #
        # Toolbar
        #

        self.scan_action.setEnabled(True)

        self.refresh_action.setEnabled(True)

        #
        # Status
        #

        self.status_widget.set_status(
            "Tarama tamamlandı."
        )

        #
        # Progress
        #

        self.progress_widget.set_progress(100)

        #
        # Sayfaları Güncelle
        #

        self.refresh_pages()

        #
        # Bilgi
        #

        QMessageBox.information(

            self,

            "Tarama Tamamlandı",

            f"""
Tarama başarıyla tamamlandı.

Klasör : {statistics['folder_count']}

Dosya : {statistics['file_count']}

Boyut : {statistics['total_size']:,} byte

Süre : {statistics['duration']} sn
            """,

        )

    # -------------------------------------------------
    # SCAN ERROR
    # -------------------------------------------------

    def scan_error(self, message):

        Logger.exception(message)

        self.scan_action.setEnabled(True)

        self.refresh_action.setEnabled(True)

        self.status_widget.set_status(
            "Tarama başarısız."
        )

        QMessageBox.critical(

            self,

            "Tarama Hatası",

            message,

        )

    # -------------------------------------------------
    # THREAD FINISHED
    # -------------------------------------------------

    def scan_thread_finished(self):

        Logger.info(
            "Scan thread kapandı."
        )

        self.worker = None

        self.thread = None

    # -------------------------------------------------
    # CLOSE EVENT
    # -------------------------------------------------

    def closeEvent(self, event):

        #
        # Tarama devam ediyor mu?
        #

        if self.thread is not None and self.thread.isRunning():

            reply = QMessageBox.question(

                self,

                "Çıkış",

                "Şu anda bir tarama devam ediyor.\n\n"
                "Yine de uygulamadan çıkmak istiyor musunuz?",

                QMessageBox.Yes | QMessageBox.No,

                QMessageBox.No,

            )

            if reply == QMessageBox.No:

                event.ignore()

                return

            #
            # Thread'i güvenli şekilde kapat
            #

            self.thread.quit()

            self.thread.wait(5000)

        Logger.info(
            "Uygulama kapatıldı."
        )

        event.accept()
            #
    # Page Indexes
    #

    PAGE_DASHBOARD = 0
    PAGE_DISKS = 1
    PAGE_FOLDERS = 2
    PAGE_FILES = 3
    PAGE_SEARCH = 4
    PAGE_ANALYSIS = 5
    PAGE_STATISTICS = 6
    PAGE_REPORTS = 7
    PAGE_SETTINGS = 8