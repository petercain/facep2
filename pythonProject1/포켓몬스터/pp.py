import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

list_of_gifs = ['test1.gif', 'test2.gif', 'test3.gif', 'test4.gif']

class GIFLabel(QLabel):
    def __init__(self, gifs, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.mGifs = gifs
        self.changeGIF()

    def changeGIF(self):
        gif = random.choice(self.mGifs)
        movie = QMovie(gif)
        self.setMovie(movie)
        movie.start()

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(600, 600)
        self.initUI()

    def initUI(self):
        self.btn = QPushButton("change", self)
        self.label = GIFLabel(list_of_gifs, self)
        self.btn.clicked.connect(self.label.changeGIF)
        self.grid = QVBoxLayout(self)
        self.grid.addWidget(self.btn)
        self.grid.addWidget(self.label)
        self.grid.addStretch(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyApp = Window()
    MyApp.show()
    sys.exit(app.exec_())