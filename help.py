import math
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)


class Help(QGroupBox):
    instance = None

    def __init__(self, parent):
        if Help.instance == None:
            super(Help, self).__init__(parent)
            self.init(parent)
            self.parent = parent
            Help.instance = self

    def getHelp(parent):
        if Help.instance == None: Help(parent)
        return Help.instance

    def init(self, parent):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(parent.widgetSize[0], parent.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

        lbl = QLabel()
        lbl.setStyleSheet("color: white")
        lbl.setFont(QFont('Serif', 14, QFont.Weight.Bold))
        lbl.setText("Press F1 for this help box\n\nPress 1 for stopwatch\nPress 2 for timer\nPress 3 for interval timer")
        layout.addWidget(lbl)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.parent.delModule(self.instance)
            self.setParent(None)