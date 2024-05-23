import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QWidget, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Four Corner Buttons with Background")
        self.setGeometry(100, 100, 800, 600)  # Initial size and position

        # Create a QLabel for the background image
        # self.background_label = QLabel(self)
        # self.background_label.setPixmap(QPixmap("second_page.jpg"))  # Replace with your image path
        # self.background_label.setScaledContents(True)
        # self.background_label.setGeometry(self.rect())
        # self.background_label.lower()

        # Central widget
        # central_widget = QWidget(self)
        # self.setCentralWidget(central_widget)

        # Grid layout
        layout = QGridLayout()

        # Create larger buttons with colors
        button_size = 150
        self.top_left_button = QPushButton("Collect", self)
        self.top_left_button.setFixedSize(button_size, button_size)
        self.top_left_button.setStyleSheet("background-color: #2E6924; color: white; font-family: Harlow; font-size: 25pt;")
       

        self.top_right_button = QPushButton("View Collection", self)
        self.top_right_button.setFixedSize(button_size, button_size)
        self.top_right_button.setStyleSheet("background-color: #B1F166; color: white; font-family: Harlow; font-size: 15pt;")

        self.bottom_left_button = QPushButton("Help", self)
        self.bottom_left_button.setFixedSize(button_size, button_size)
        self.bottom_left_button.setStyleSheet("background-color: #E9EF8B; color: white; font-family: Harlow; font-size: 25pt;")

        self.bottom_right_button = QPushButton("Restart", self)
        self.bottom_right_button.setFixedSize(button_size, button_size)
        self.bottom_right_button.setStyleSheet("background-color: #04EC1B; color: black; font-family: Harlow; font-size: 25pt;")

        # Add buttons to the grid layout
        layout.addWidget(self.top_left_button, 0, 0, alignment=Qt.AlignTop | Qt.AlignLeft)
        layout.addWidget(self.top_right_button, 0, 1, alignment=Qt.AlignTop | Qt.AlignRight)
        layout.addWidget(self.bottom_left_button, 1, 0, alignment=Qt.AlignBottom | Qt.AlignLeft)
        layout.addWidget(self.bottom_right_button, 1, 1, alignment=Qt.AlignBottom | Qt.AlignRight)

        self.setLayout(layout)

    # def resizeEvent(self, event):
    #     self.background_label.setGeometry(self.rect())
    #     super().resizeEvent(event)  # Call the base implementation to ensure normal processing

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Menu()
    window.show()
    app.exec()
