import math
from win10toast import ToastNotifier
from PyQt6.QtCore import QTimer, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (QGroupBox, QLabel, QVBoxLayout)

class Interval(QGroupBox):
    flag = False
    count = 0
    position = 0
    waitingInput = False
    interval = 0
    toast = ToastNotifier()

    def __init__(self, parent):
        super(Interval, self).__init__(parent)
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
        layout.addWidget(lbl)

        timer = QTimer(self)
        timer.timeout.connect(self.calcTime)
        timer.start(10)

    def mousePressEvent(self, QMouseEvent):
        if self.waitingInput:
            if QMouseEvent.button() == Qt.MouseButton.LeftButton:
                self.lblChange(1)
            elif QMouseEvent.button() == Qt.MouseButton.RightButton:
                self.lblChange(-1)
            elif QMouseEvent.button() == Qt.MouseButton.MiddleButton:
                self.position += 1
                if self.position > 3:
                    self.count = (int(self.lbl.text()[0]) * 60000) + (int(self.lbl.text()[1]) * 6000) + (int(self.lbl.text()[3]) * 1000) + (int(self.lbl.text()[4]) * 100)
                    self.interval = self.count
                    self.flag = False
                    self.waitingInput = False
                    self.position = 0
        else:
            if QMouseEvent.button() == Qt.MouseButton.LeftButton:
                if self.count == 0:
                    self.waitingInput = True
                    self.lbl.setFont(QFont('Serif', 44, QFont.Weight.Bold))
                    self.lbl.setText("00:00:xx")
                self.flag = not self.flag
            elif QMouseEvent.button() == Qt.MouseButton.RightButton:
                self.reset()
            elif QMouseEvent.button() == Qt.MouseButton.MiddleButton:
                self.parent.delModule(self)

    def calcTime(self):
        if self.flag: self.count -= 1
        if not self.waitingInput:
            if self.count == 1:
                self.toast.show_toast("Interval lap!","Your set interval just made a lap!",duration=10, threaded=True)
            elif self.count == 0 and self.flag == False:
                self.lbl.setFont(QFont('Serif', 32, QFont.Weight.Bold))
                self.lbl.setText("Set interval")
            elif self.count < 0:
                self.count = self.interval
            else:
                self.lbl.setFont(QFont('Serif', 44, QFont.Weight.Bold))
                t = ["00", ":", "00", ":", "00"]
                if self.count % 100 < 10: t[4] = "0" + str(self.count % 100)
                else: t[4] = str(self.count % 100)
                if math.floor((self.count % 6000) / 100) < 10: t[2] = "0" + str(math.floor((self.count % 6000) / 100))
                else: t[2] = str(math.floor((self.count % 6000) / 100))
                if math.floor(self.count / 6000) < 10: t[0] = "0" + str(math.floor(self.count / 6000))
                else: t[0] = str(math.floor(self.count / 6000))
                self.lbl.setText("".join(t))

    def lblChange(self, num):
        match self.position:
            case 0:
                num = int(self.lbl.text()[0]) + num
                if num < 0: num = "0"
                elif num > 5: num = "5"
                else: num = str(num)
                self.lbl.setText(num + self.lbl.text()[1:])
            case 1: 
                num = int(self.lbl.text()[1]) + num
                if num < 0: num = "0"
                elif num > 9: num = "9"
                else: num = str(num)
                self.lbl.setText(self.lbl.text()[:1] + num + self.lbl.text()[2:])
            case 2: 
                num = int(self.lbl.text()[3]) + num
                if num < 0: num = "0"
                elif num > 5: num = "5"
                else: num = str(num)
                self.lbl.setText(self.lbl.text()[:3] + num + self.lbl.text()[4:])
            case 3: 
                num = int(self.lbl.text()[4]) + num
                if num < 0: num = "0"
                elif num > 9: num = "9"
                else: num = str(num)
                self.lbl.setText(self.lbl.text()[:4] + num + self.lbl.text()[5:])

    def reset(self):
        self.flag = False
        self.count = 0