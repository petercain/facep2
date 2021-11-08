import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

form_class = uic.loadUiType("cat.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.timer = QTimer(self)
        self.timer.start(9000)
        self.timer.timeout.connect(self.sshow)

    def sshow(self):
        f = 'GIF1.gif'
        h = 'b2.gif'
        i = 'c3.gif'
        j = 'f4.gif'
        k = 'k6.gif'
        m = 'n6.gif'
        n = 'ca1.gif'
        a1 = 'abc1.gif'
        a2 = 'abc2.gif'
        a3 = 'abc3.gif'
        a4 = 'abc4.gif'
        a5 = 'abc5.gif'
        a6 = 'abc6.gif'
        a7 = 'abc7.gif'
        a8 = 'abc8.gif'
        a9 = 'abc9.gif'
        a10 = 'abc10.gif'
        a11 = 'abc11.gif'
        a12 = 'abc12.gif'
        b1 = 'new1.gif'
        b2 = 'new2.gif'
        b3 = 'new3.gif'
        b4 = 'new4.gif'
        b5 = 'new5.gif'
        b6 = 'new6.gif'

        self.listm = [f, h, i, j, k, m, n, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, b1, b2, b3, b4, b5, b6]
        X = random.choice(self.listm)
        self.movie = QMovie(X)
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()