from PySide6.QtCore import Qt
from PySide6.QtGui import QAction

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QListWidgetItem,
    QLabel,
    QPushButton,
    QStackedWidget,
    QFrame,
    QStatusBar,
    QSizePolicy,
)

from ui.dashboard import DashboardPage
from ui.task_page import TaskPage
from ui.log_page import LogPage
from ui.settings_page import SettingsPage


class MainWindow(QMainWindow):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Amazon Scraper Pro")

        self.resize(1400, 850)

        self.build_ui()

    def build_ui(self):

        root = QWidget()

        self.setCentralWidget(root)

        layout = QHBoxLayout(root)

        layout.setContentsMargins(0, 0, 0, 0)

        layout.setSpacing(0)

        # -----------------------------
        # Sidebar
        # -----------------------------

        sidebar = QFrame()

        sidebar.setFixedWidth(220)

        sidebar.setObjectName("Sidebar")

        sidebar_layout = QVBoxLayout(sidebar)

        sidebar_layout.setContentsMargins(15, 20, 15, 20)

        sidebar_layout.setSpacing(12)

        title = QLabel("Amazon Scraper Pro")

        title.setAlignment(Qt.AlignCenter)

        title.setStyleSheet("""
            font-size:18px;
            font-weight:bold;
        """)

        sidebar_layout.addWidget(title)

        self.menu = QListWidget()

        self.menu.addItem(QListWidgetItem("🏠 Dashboard"))
        self.menu.addItem(QListWidgetItem("📋 Tasks"))
        self.menu.addItem(QListWidgetItem("📜 Logs"))
        self.menu.addItem(QListWidgetItem("⚙ Settings"))

        self.menu.setCurrentRow(0)

        sidebar_layout.addWidget(self.menu)

        sidebar_layout.addStretch()

        version = QLabel("Version 0.1")

        version.setAlignment(Qt.AlignCenter)

        sidebar_layout.addWidget(version)

        # -----------------------------
        # Pages
        # -----------------------------

        self.stack = QStackedWidget()

        self.dashboard = DashboardPage()

        self.tasks = TaskPage()

        self.logs = LogPage()

        self.settings = SettingsPage()

        self.stack.addWidget(self.dashboard)
        self.stack.addWidget(self.tasks)
        self.stack.addWidget(self.logs)
        self.stack.addWidget(self.settings)

        layout.addWidget(sidebar)

        layout.addWidget(self.stack)

        self.menu.currentRowChanged.connect(self.stack.setCurrentIndex)

        # -----------------------------
        # Status Bar
        # -----------------------------

        status = QStatusBar()

        self.setStatusBar(status)

        status.showMessage("Ready")

        self.apply_theme()

    def apply_theme(self):

        self.setStyleSheet("""

        QMainWindow{

            background:#1e1e1e;

        }

        QLabel{

            color:white;

        }

        QFrame#Sidebar{

            background:#252526;

        }

        QListWidget{

            background:#252526;

            color:white;

            border:none;

            font-size:14px;

        }

        QListWidget::item{

            padding:12px;

            border-radius:6px;

        }

        QListWidget::item:selected{

            background:#007ACC;

        }

        QListWidget::item:hover{

            background:#2d2d30;

        }

        QStatusBar{

            background:#252526;

            color:white;

        }

        """)
