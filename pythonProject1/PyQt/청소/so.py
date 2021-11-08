import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

form_class = uic.loadUiType("so.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.AI2 = [ 3, 4, 5, 6, 7, 8, 9, 10, 12, 2, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        self.pushButton.clicked.connect(self.sakura)

    def sakura(self):
        a = 'sakura.gif'
        b = 'gogog.gif'
        c = 'dance (1).gif'
        d = 'dance (2).gif'
        e = 'dance (3).gif'
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
        self.listm = [a, b, c, d, e, f, h, i, j, k, m, n, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12]
        X = random.choice(self.listm)
        self.kdialog.show()
        self.movie = QMovie(X)
        self.label_4.setMovie(self.movie)
        self.movie.start()
        QTimer.singleShot(1000, self.cleaning)
        QTimer.singleShot(1000, self.seco)
        QTimer.singleShot(6000, self.boom)

    def boom(self):
        self.kdialog.close()

    def cleaning(self):
        for i in range(3):
            X = random.choice(self.AI2)
            self.AI2.remove(X)
            self.textBrowser.append("{}".format(X))

    def seco(self):
        for l in range(2):
            X = random.choice(self.AI2)
            self.AI2.remove(X)
            self.textBrowser_2.append("{}".format(X))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()