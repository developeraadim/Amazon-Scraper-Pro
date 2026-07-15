from PySide6.QtCore import Qt

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout,
)


class DashboardPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QVBoxLayout(self)

        layout.setAlignment(Qt.AlignTop)

        title = QLabel("Dashboard")

        title.setStyleSheet("""
            font-size:26px;
            font-weight:bold;
            color:white;
        """)

        layout.addWidget(title)

        upload = QPushButton("Upload Excel")

        upload.setMinimumHeight(50)

        layout.addWidget(upload)

        layout.addStretch()
