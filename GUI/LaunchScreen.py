import sys
import signal
from pathlib import Path
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QWidget,
    QSizePolicy
)
from PyQt5.QtGui import QImage, QPainter

from menu_screen import Menu

# Main window class
class LaunchScreen(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Zoodex Home page")  # Set the title of the window
        
        # Create a layout for the central widget
        self.layout = QVBoxLayout()
        # self.layout.setGeometry
        self.layout.addStretch()
        self.layout.setSpacing(0)
        self.setContentsMargins(0,0,0,0)

        # Create a QLabel to be centered
        self.center_label = QLabel("ZOODEX", self)
        
        # Center the label using the layout
        self.layout.addWidget(self.center_label, 0, QtCore.Qt.AlignCenter) #, alignment=Qt.AlignCenter)

        self.layout.addSpacing(75)

        # Create a button
        self.start_button = QPushButton("Tap to Start!", self)
        # start_button.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.start_button.setFixedSize(200,100)
        self.start_button.setObjectName("start")
        # start_button.clicked.connect(self.show_menu)  # Connect button click to function
        self.layout.addWidget(self.start_button, 0, QtCore.Qt.AlignHCenter)  # Add the button to the layout

        self.layout.addSpacing(20)

        # Set the layout for the central widget
        # central_widget.setLayout(self.layout)

        self.setLayout(self.layout)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)


    # Main application logic
    app = QApplication(sys.argv)  # Initialize the application
    app.setStyleSheet(Path('styles.qss').read_text())
    window = LaunchScreen()  # Create the main window
    window.show()  # Show the main window
    app.exec()  # Start the event loop