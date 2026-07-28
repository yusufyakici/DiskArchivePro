"""
DiskArchive Pro v2
Application Entry Point
"""

import sys

from PySide6.QtWidgets import QApplication

from app.config.config import Config
from app.database.database import Database
from app.gui.main_window import MainWindow
from app.utils.logger import Logger


def main():

    # -------------------------------------------------
    # Initialize
    # -------------------------------------------------

    Config.initialize()

    Logger.initialize()

    db = Database()

    # -------------------------------------------------
    # Qt Application
    # -------------------------------------------------

    app = QApplication(sys.argv)

    app.setApplicationName(
        Config.APP_NAME
    )

    app.setApplicationVersion(
        Config.VERSION
    )

    # -------------------------------------------------
    # Main Window
    # -------------------------------------------------

    window = MainWindow(db)

    window.show()

    # -------------------------------------------------
    # Run
    # -------------------------------------------------

    exit_code = app.exec()

    db.close()

    sys.exit(exit_code)


if __name__ == "__main__":

    main()