import sys
import json

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon, QImage, QPixmap, QPainter
from PyQt5 import QtCore

class Animal(QWidget):
    data = {}

    def __init__(self, data = {}, animal):
        super().__init__()

        self.data = data

        self.layout = QGridLayout()
        
        # self.animals = {
        #     "tiger": QPushButton('', self),
        #     "african_elephant": QPushButton('', self),
        #     "zebra": QPushButton('', self),
        #     "gorilla": QPushButton('', self),
        #     "giant_panda": QPushButton('', self),
        #     "cheetah": QPushButton('', self),
        #     "great_white_shark": QPushButton('', self),
        #     "starfish": QPushButton('', self),
        #     "stingray": QPushButton('', self),
        #     "leatherback_turtle": QPushButton('', self)
        # }

        self.image = QLabel(self)

        self.image.setPixmap(QPixmap.fromImage(f"../collection/images/collected/{animal}.png"))

        # for animal in self.data:
        #     for info in self.data[animal]:
        #         if info.get("collected") == "true":
        #             self.animals[animal].setIcon(QIcon(f'../collection/images/collected/{animal}.png'))
        #         else:
        #             self.animals[animal].setIcon(QIcon(f'../collection/images/silhouette/{animal}.png'))
                
        #         self.animals[animal].setIconSize(QtCore.QSize(100, 100))

        # top_row = dict(list(self.animals.items())[:len(self.animals)//2])
        # bottom_row = dict(list(self.animals.items())[len(self.animals)//2:])

        # for i, (_, v) in enumerate(top_row.items()):
        #     self.layout.addWidget(v, 0, i)

        # for i, (_, v) in enumerate(bottom_row.items()):
        #     self.layout.addWidget(v, 1, i)

        self.layout.addWidget()

        self.menu = QPushButton("Menu", self)
        self.menu.resize(100, 100)
        self.menu.setObjectName("start")
        self.layout.addWidget(self.menu, 2, 2)
     
        self.setLayout(self.layout)

    def set_collected(self, animal):
        if self.data is not None:
            self.data[animal][0].update({"collected": "true"})

if __name__ == "__main__":
    app = QApplication(sys.argv)

    scrn = Collection()

    scrn.show()

    app.exec()