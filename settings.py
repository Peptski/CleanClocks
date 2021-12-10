from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)

class Settings(QGroupBox):
    widgetSize = [256, 144]
    instance = None

    def __init__(self, parent):
        if Settings.instance == None:
            super(Settings, self).__init__(parent)
            self.init()
            self.parent = parent
            Settings.instance = self

    def getSettings(parent):
        if Settings.instance == None: Settings(parent)
        return Settings.instance

    def init(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(self.widgetSize[0], self.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

        lbl = QLabel()
        self.lbl = lbl
        lbl.setStyleSheet("color: white")
        lbl.setFont(QFont('Serif', 43, QFont.Weight.Bold))
        lbl.setText("Settings")
        layout.addWidget(lbl)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.parent.delModule(self.instance)
            self.setParent(None)