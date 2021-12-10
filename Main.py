import sys
from stopwatch import Stopwatch
from settings import Settings
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

        settings = QAction(self)
        settings.setShortcut("h")
        settings.triggered.connect(self.initSettings)
        self.menuBar().addAction(settings)

        stopwatch = QAction(self)
        stopwatch.setShortcut("Ctrl+1")
        stopwatch.triggered.connect(self.initStopwatch)
        self.menuBar().addAction(stopwatch)

        qr = self.frameGeometry()
        qr.moveCenter(self.screen().availableGeometry().center())
        self.move(qr.topLeft())
        self.setWindowTitle("QoL")
        self.setStyleSheet("background-color: #282828")

        self.show()

    def delModule(self, module):
        self.layout.removeWidget(module)
        self.setStyleSheet("background-color: #282828")

    def initSettings(self):
        settings = Settings.getSettings(self)
        self.layout.addWidget(settings)

    def initStopwatch(self):
        stopwatch = Stopwatch(self)
        self.layout.addWidget(stopwatch)

def main():
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()