import sys
from PyQt5 import  QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5 import uic

UI = '포켓몬.ui'

class window1(QDialog):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(UI, self)

        self.pushButton.setIcon(QtGui.QIcon('오구.jpg'))

app = QApplication(sys.argv)
a = window1()
a.show()
app.exec_()
