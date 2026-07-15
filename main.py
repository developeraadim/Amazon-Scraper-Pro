import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

from ui.main_window import MainWindow


def main():

    app = QApplication(sys.argv)

    app.setApplicationName("Amazon Scraper Pro")
    app.setOrganizationName("DeveloperAadi")

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
