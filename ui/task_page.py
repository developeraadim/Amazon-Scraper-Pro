from PySide6.QtWidgets import QWidget,QVBoxLayout,QLabel


class TaskPage(QWidget):

    def __init__(self):

        super().__init__()

        layout=QVBoxLayout(self)

        layout.addWidget(QLabel("Tasks"))
