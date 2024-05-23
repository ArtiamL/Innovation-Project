import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore

from image_classification.classify import Thread
from collection import Collection
import json
# import image_classification.classify as classify

class Camera(QWidget):
    thread = None
    data = ""

    def __init__(self, data):
        super().__init__()

        self.data = data

        # print(self.data)
        
        self.label = QLabel(self)
        self.label.resize(640, 480)

        self.button = QPushButton("View Collection", self)
        self.button.setFixedSize(250,100)

        self.layout = QVBoxLayout()
        self.layout.addStretch()
        self.layout.setSpacing(0)
        self.setContentsMargins(0,0,0,0)

        self.layout.addWidget(self.label, 0, QtCore.Qt.AlignCenter)
        self.layout.addSpacing(75)
        self.layout.addWidget(self.button, 0, QtCore.Qt.AlignHCenter)
        self.layout.addSpacing(20)

        self.setLayout(self.layout)

    def start_thread(self):
        self.thread = Thread(self)
        self.thread.changePixmap.connect(self.setImage)
        self.thread.collected.connect(self.show_collected)
        self.thread.run('../image_classification/mobilenet_v2.tflite', 1, 9, 4, False, 0, 480, 640)

    @QtCore.pyqtSlot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))

    @QtCore.pyqtSlot(str, name='collected')
    def show_collected(self, animal):
        print(f"Collected: {animal}")
        self.thread.stop()
        self.label.clear()
        self.label.setText("Collected!")
        self.label.setObjectName("start")
        self.layout.addSpacing(75)
        self.layout.addWidget(self.button, 0, QtCore.Qt.AlignHCenter)
        self.layout.addSpacing(20)


        print(self.data[animal][0])
        self.data[animal][0]["collected"] = "true"

        with open("../collection/data/animals.json", "w") as f:
            json.dump(self.data, f)

        # self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    cam = Camera()

    cam.start_thread()

    cam.show()