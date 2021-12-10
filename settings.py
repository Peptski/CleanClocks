import math
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)


class Settings(QGroupBox):
    widgetSize = [256, 144]

    def __init__(self, parent):
        super(Settings, self).__init__(parent)
        self.parent = parent
        self.init()

    def init(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(self.widgetSize[0], self.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.remove()

    def remove(self):
        self.parent.delModule(self)