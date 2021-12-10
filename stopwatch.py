import math
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)


class Stopwatch(QGroupBox):
    widgetSize = [256, 144]
    lbl = None
    flag = False
    count = 0

    def __init__(self, parent):
        super(Stopwatch, self).__init__(parent)
        self.parent = parent
        self.init()

    def init(self):
        layout = QVBoxLayout()
        self.setLayout(layout)
        self.setFixedSize(self.widgetSize[0], self.widgetSize[1])
        self.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

        lbl = QLabel()
        self.lbl = lbl
        lbl.setStyleSheet("color: white")
        lbl.setFont(QFont('Serif', 43, QFont.Weight.Bold))
        lbl.setText("00:00:00")
        layout.addWidget(lbl)

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(10)

    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.MouseButton.RightButton:
            self.reset()
        elif QMouseEvent.button() == Qt.MouseButton.MiddleButton:
            self.remove()
        else:
            self.startStop()

    def calcTime(self, count):
        t = ["00", ":", "00", ":", "00"]
        if count % 100 < 10: t[4] = "0" + str(count % 100)
        else: t[4] = str(count % 100)
        if math.floor((count % 6000) / 100) < 10: t[2] = "0" + str(math.floor((count % 6000) / 100))
        else: t[2] = str(math.floor((count % 6000) / 100))
        if math.floor(count / 6000) < 10: t[0] = "0" + str(math.floor(count / 6000))
        else: t[0] = str(math.floor(count / 6000))
        return "".join(t)

    def showTime(self):
        if self.flag:
            self.count += 1
        self.lbl.setText(self.calcTime(self.count))

    def startStop(self):
        self.flag = not self.flag
  
    def reset(self):
        self.flag = False
        self.count = 0
        self.lbl.setText("00:00:00")

    def remove(self):
        self.parent.delModule(self)