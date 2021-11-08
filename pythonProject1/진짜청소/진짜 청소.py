import sys
import random
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *

pageOneUi = 'cleaning.ui'
pageTwoUi = 'umjjal.ui'

class pageOne(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(pageOneUi, self)

        self.pushButton.clicked.connect(self.randum)

        self.AI2 = ["문영준", "박지균", "장재원", "고재범", "김상희", "함진희", "전승현", "김호현", "박문오","홍성민", "박정선", "박찬호", "신지수", "오병수", "조광렬", "황은하", "조찬익","서혜솔"]

    def randum(self):
        self.bs = pageTwo()
        self.bs.show()
        self.close()
        QTimer.singleShot(1000, self.boom)

    def boom(self):
        for i in range(3):
            X = random.choice(self.AI2)
            self.AI2.remove(X)
            self.textBrowser.append(X)

        for y in range(2):
            Y = random.choice(self.AI2)
            self.AI2.remove(Y)
            self.textBrowser_2.append(Y)
        self.bs.close()
        self.show()





class pageTwo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(pageTwoUi, self)


        self.movie = QMovie("sq.gif")
        self.label.setMovie(self.movie)
        self.movie.start()




app = QApplication(sys.argv)
ch = pageOne()
ch.show()
app.exec_()
