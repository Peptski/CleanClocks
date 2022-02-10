import sys
from stopwatch import Stopwatch
from timer import Timer
from interval import Interval
from help import Help
from PyQt6.QtWidgets import (QGridLayout, QWidget, QApplication, QMainWindow)
from PyQt6.QtGui import QAction


class Window(QMainWindow):
    widgetSize = [256, 144]
    layout = QGridLayout()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        w = QWidget(self)
        self.setCentralWidget(w)
        w.setLayout(self.layout)

        ### Start of modules

        help = QAction(self)
        help.setShortcut("F1")
        help.triggered.connect(self.initHelp)
        self.menuBar().addAction(help)

        stopwatch = QAction(self)
        stopwatch.setShortcut("1")
        stopwatch.triggered.connect(self.initStopwatch)
        self.menuBar().addAction(stopwatch)

        timer = QAction(self)
        timer.setShortcut("2")
        timer.triggered.connect(self.initTimer)
        self.menuBar().addAction(timer)

        interval = QAction(self)
        interval.setShortcut("3")
        interval.triggered.connect(self.initInterval)
        self.menuBar().addAction(interval)

        self.initHelp()

        ### End of modules

        qr = self.frameGeometry()
        qr.moveCenter(self.screen().availableGeometry().center())
        self.move(qr.topLeft())
        self.setWindowTitle("CleanClocks")
        self.setStyleSheet("background-color: #282828")
        self.adjustSize()

        self.show()

    def delModule(self, module):
        self.layout.removeWidget(module)
        self.adjustSize()

    def adjustSize(self):
        if self.layout.count() == 0: self.setFixedSize(276, 164)
        else: self.setFixedSize(276, 164 + (152 * (self.layout.count() - 1)))

    def initHelp(self):
        help = Help.getHelp(self)
        self.layout.addWidget(help)
        self.adjustSize()

    def initStopwatch(self):
        stopwatch = Stopwatch(self)
        self.layout.addWidget(stopwatch)
        self.adjustSize()

    def initTimer(self):
        timer = Timer(self)
        self.layout.addWidget(timer)
        self.adjustSize()

    def initInterval(self):
        interval = Interval(self)
        self.layout.addWidget(interval)
        self.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()