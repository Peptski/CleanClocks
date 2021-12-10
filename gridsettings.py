from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QPushButton, QTableWidget, QVBoxLayout, QWidget)

class Gridsettings(QGroupBox):
    instance = None

    def __init__(self, parent):
        if Gridsettings.instance == None:
            super(Gridsettings, self).__init__(parent)
            self.init(parent)
            self.parent = parent
            Gridsettings.instance = self

    def getSettings(parent):
        if Gridsettings.instance == None: Gridsettings(parent)
        return Gridsettings.instance

    def init(self, parent):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(parent.widgetSize[0], parent.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.parent.delModule(self.instance)
            self.setParent(None)