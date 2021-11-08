import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

pageOneUi = 'one.ui'
pageTwoUi = 'two.ui'

class page_2(QWidget):

    def __init__(self):
        super().__init__(self, None)
        uic.loadUi(pageTwoUi, self)

class page_1(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi(pageOneUi, self)

app = QApplication(sys.argv)
ch = page_1()
ch.show()
app.exec_()