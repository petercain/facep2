import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

pageOneUi = 'one.ui'
pageTwoUi = 'two.ui'

class pageTwo(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageTwoUi, self)


        self.pushButton_1.clicked.connect(self.ddown)

    def ddown(self):
        self.close()


class pageOne(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(pageOneUi, self)

        self.pushButton.clicked.connect(self.sshow)

    def sshow(self):
        self.ch = pageTwo()
        self.ch.show()
        self.close()


app = QApplication(sys.argv)
ch = pageOne()
ch.show()
app.exec_()