import sys
import signal
from pathlib import Path
import json

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedLayout, QLabel, QWidget
from PyQt5.QtGui import QPixmap, QImage, QPainter

from LaunchScreen import LaunchScreen
from menu_screen import Menu
from camera import Camera
from collection import Collection

class MainWindow(QMainWindow):
    data = {}

    def __init__(self):
        super().__init__()

        with open("../collection/data/animals.json", "r") as f:
            self.data = json.load(f)

        # print(self.data)

        self.setObjectName("bgLaunch")

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        
        self.stacked = QStackedLayout()

        self.launch = LaunchScreen()
        self.launch.start_button.clicked.connect(self.show_menu)

        self.menu = Menu()
        self.menu.top_left_button.clicked.connect(self.show_camera)
        self.menu.top_right_button.clicked.connect(self.show_collection)
        self.menu.bottom_right_button.clicked.connect(self.restart)

        self.camera = Camera(self.data)
        self.camera.button.clicked.connect(self.show_collection)

        self.collection = Collection(self.data)
        self.collection.menu.clicked.connect(self.show_menu)

        self.stacked.addWidget(self.launch)
        self.stacked.addWidget(self.menu)
        self.stacked.addWidget(self.camera)
        self.stacked.addWidget(self.collection)
        self.stacked.setCurrentIndex(0)

        widget = QWidget()
        widget.setLayout(self.stacked)
        self.setCentralWidget(widget)

        self.showFullScreen()

    def show_menu(self):
        self.stacked.setCurrentIndex(1)
        self.setObjectName("bgMenu")
        self.style().unpolish(self)
        self.style().polish(self)

    def show_camera(self):
        self.stacked.setCurrentIndex(2)
        self.camera.start_thread()

    def show_collection(self):
        self.stacked.setCurrentIndex(3)
        self.setObjectName("bgMenu")
        self.style().unpolish(self)
        self.style().polish(self)

    def restart(self):
        self.stacked.setCurrentIndex(0)
        self.setObjectName("bgLaunch")
        self.style().unpolish(self)
        self.style().polish(self)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)


    # Main application logic
    app = QApplication(sys.argv)  # Initialize the application
    app.setStyleSheet(Path('styles.qss').read_text())
    app.setOverrideCursor(Qt.BlankCursor)
    window = MainWindow()  # Create the main window
    window.show()  # Show the main window
    app.exec()  # Start the event loop