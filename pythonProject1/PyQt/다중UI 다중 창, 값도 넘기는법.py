import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

one = 'new1.ui'
two = 'new2.ui'

class window2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(two, self)

        self.show()

class window1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(one, self)
        self.window2 = window2() # 페이지 2번에 값을 넘기기 위해 선언한 것

        self.pushButton.clicked.connect(self.nextpage)

    def nextpage(self):
        self.window2.listWidget.addItem(self.lineEdit.text()) # 값을 넘기는 것

        self.window2.show() # 페이지 전환 것
        self.close()

app = QApplication(sys.argv)
ss = window1()
ss.show()
app.exec_()