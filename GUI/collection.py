import sys
import json

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class Collection(QWidget):
    data = {}

    def __init__(self):
        super().__init__()

        with open("../collection/data/animals.json", "r") as f:
            self.data = json.load(f)

        self.layout = QGridLayout()
        
        self.animals = {
            "tiger": QPushButton('', self),
            "african_elephant": QPushButton('', self),
            "zebra": QPushButton('', self),
            "gorilla": QPushButton('', self),
            "giant_panda": QPushButton('', self),
            "cheetah": QPushButton('', self),
            "great_white_shark": QPushButton('', self),
            "starfish": QPushButton('', self),
            "stingray": QPushButton('', self),
            "turtle": QPushButton('', self)
        }

        for animal in self.data:
            for info in self.data[animal]:
                if info.get("collected") == "true":
                    self.animals[animal].setIcon(QIcon(f'../collection/images/collected/{animal}.png'))
                else:
                    self.animals[animal].setIcon(QIcon(f'../collection/images/silhouette/{animal}.png'))
                
                self.animals[animal].setIconSize(QtCore.QSize(100, 100))

        top_row = dict(list(self.animals.items())[:len(self.animals)//2])
        bottom_row = dict(list(self.animals.items())[len(self.animals)//2:])

        for i, (_, v) in enumerate(top_row.items()):
            self.layout.addWidget(v, 0, i)

        for i, (_, v) in enumerate(bottom_row.items()):
            self.layout.addWidget(v, 1, i)
     
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    scrn = Collection()

    scrn.show()

    app.exec()