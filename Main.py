import sys
from stopwatch import Stopwatch
from gridsettings import Gridsettings
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

        gridsettings = QAction(self)
        gridsettings.setShortcut("h")
        gridsettings.triggered.connect(self.initSettings)
        self.menuBar().addAction(gridsettings)

        stopwatch = QAction(self)
        stopwatch.setShortcut("1")
        stopwatch.triggered.connect(self.initStopwatch)
        self.menuBar().addAction(stopwatch)

        qr = self.frameGeometry()
        qr.moveCenter(self.screen().availableGeometry().center())
        self.move(qr.topLeft())
        self.setWindowTitle("QoL")
        self.setStyleSheet("background-color: #282828")
        self.adjustSize()

        self.show()

    def delModule(self, module):
        self.layout.removeWidget(module)
        self.adjustSize()

    def adjustSize(self):
        if self.layout.count() == 0: self.setFixedSize(276, 164)
        else: self.setFixedSize(276, 164 + (152 * (self.layout.count() - 1)))

    def initSettings(self):
        settings = Gridsettings.getSettings(self)
        self.layout.addWidget(settings)
        self.adjustSize()

    def initStopwatch(self):
        stopwatch = Stopwatch(self)
        self.layout.addWidget(stopwatch)
        self.adjustSize()

def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()