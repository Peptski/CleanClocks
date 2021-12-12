import math
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)


class Stopwatch(QGroupBox):
    flag = False
    count = 0

    def __init__(self, parent):
        super(Stopwatch, self).__init__(parent)
        self.parent = parent
        self.init(parent)

    def init(self, parent):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(parent.widgetSize[0], parent.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

        lbl = QLabel()
        self.lbl = lbl
        lbl.setStyleSheet("color: white")
        lbl.setFont(QFont('Serif', 43, QFont.Weight.Bold))
        layout.addWidget(lbl)

        timer = QTimer(self)
        timer.timeout.connect(self.calcTime)
        timer.start(10)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.LeftButton:
            self.flag = not self.flag
        elif QMouseEvent.button() == Qt.MouseButton.RightButton:
            self.flag = False
            self.count = 0
            self.lbl.setText("00:00:00")
        elif QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.parent.delModule(self)

    def calcTime(self):
        if self.flag: self.count += 1
        t = ["00", ":", "00", ":", "00"]
        if self.count % 100 < 10: t[4] = "0" + str(self.count % 100)
        else: t[4] = str(self.count % 100)
        if math.floor((self.count % 6000) / 100) < 10: t[2] = "0" + str(math.floor((self.count % 6000) / 100))
        else: t[2] = str(math.floor((self.count % 6000) / 100))
        if math.floor(self.count / 6000) < 10: t[0] = "0" + str(math.floor(self.count / 6000))
        else: t[0] = str(math.floor(self.count / 6000))
        self.lbl.setText("".join(t))