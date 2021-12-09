from ctypes import alignment
import sys
import math
from PyQt6.QtWidgets import (QGridLayout, QGroupBox, QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout, QMainWindow)
from PyQt6.QtCore import QDate, QTimer
from PyQt6.QtGui import QAction, QFont, QMouseEvent


class Window(QMainWindow):
    widgetSize = [256, 144]
    layout = QGridLayout()
    initialized = [0, 0]
    stopwatchFlag = False
    stopwatchCount = 0
    stopwatchLabel = "00:00:00"

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        self.setCentralWidget(w)
        w.setLayout(self.layout)

        menubar = self.menuBar()
        newMenu = menubar.addMenu("New")

        stopwatchAction = QAction("Stopwatch", self)
        stopwatchAction.setShortcut("Ctrl+1")
        stopwatchAction.triggered.connect(self.initStopwatch)

        timerAction = QAction("Timer", self)
        timerAction.setShortcut("Ctrl+2")
        timerAction.triggered.connect(self.stopwatchStartStop)

        newMenu.addAction(stopwatchAction)
        newMenu.addAction(timerAction)

        menubar.setStyleSheet("background-color: #212121; color: white")

        self.initStopwatch()

        qr = self.frameGeometry()
        qr.moveCenter(self.screen().availableGeometry().center())
        self.move(qr.topLeft())
        self.setWindowTitle("QoLApp")
        self.setStyleSheet("background-color: #282828")

        self.show()

    def initStopwatch(self):
        if not self.initialized[0]:
            stopWatch = QGroupBox()
            stopWatchLayout = QVBoxLayout()
            stopWatch.setLayout(stopWatchLayout)
            stopWatch.setFixedSize(self.widgetSize[0], self.widgetSize[1])
            stopWatch.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

            lbl = QLabel()
            self.stopwatchLabel = lbl
            lbl.setStyleSheet("color: white")
            lbl.setFont(QFont('Serif', 43, QFont.Weight.Bold))
            stopWatchLayout.addWidget(lbl)

            self.layout.addWidget(stopWatch)
    
            timer = QTimer(self)
            timer.timeout.connect(self.showTime)
            timer.start(10)

            self.initialized[0] = 1

    def showTime(self):
        if self.stopwatchFlag:
            self.stopwatchCount += 1
        t = ["00", ":", "00", ":", "00"]
        if self.stopwatchCount % 100 < 10: t[4] = "0" + str(self.stopwatchCount % 100)
        else: t[4] = str(self.stopwatchCount % 100)
        if math.floor((self.stopwatchCount % 6000) / 100) < 10: t[2] = "0" + str(math.floor((self.stopwatchCount % 6000) / 100))
        else: t[2] = str(math.floor((self.stopwatchCount % 6000) / 100))
        if math.floor(self.stopwatchCount / 6000) < 10: t[0] = "0" + str(math.floor(self.stopwatchCount / 6000))
        else: t[0] = str(math.floor(self.stopwatchCount / 6000))
        self.stopwatchLabel.setText("".join(t))
  
    def stopwatchStartStop(self):
        self.stopwatchFlag = not self.stopwatchFlag
  
    def stopwatchReset(self):
        self.stopwatchFlag = False
        self.stopwatchCount = 0
        self.stopwatchLabel.setText("00:00:00")

    def initTimer(self):
        if not self.initialized[1]:
            timer = QGroupBox()
            timerLayout = QVBoxLayout()
            timer.setLayout(timerLayout)
            timer.setFixedSize(self.widgetSize[0], self.widgetSize[1])
            timer.setStyleSheet("background-color: #212121; border: 0px; border-radius: 20px")

            self.layout.addWidget(timer)

            self.initialized[1] = 1

def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()