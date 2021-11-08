import sys
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

pageOneUi = 'kosk.ui'
pageTwoUi = 'chage.ui'

class variable:
    totalmoney = 0

class pageTwo(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageTwoUi, self)

        self.movie = QMovie("sakura.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        self.pushButton_4.clicked.connect(self.cchage)

    def cchage(self):
        self.pageOne=pageOne()
        self.pageOne.listWidget.addItem("{}".format(variable.totalmoney + 5))
        self.pageOne.show()
        self.close()

class pageOne(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageOneUi, self)


        self.pushButton.clicked.connect(self.amechu)
        self.pushButton_2.clicked.connect(self.bschu)
        self.pushButton_3.clicked.connect(self.sshow)
        self.listWidget.itemDoubleClicked.connect(self.cm)

    def amechu(self):
        self.listWidget.addItem("아메리카노 : 3000")
        variable.totalmoney += 3000

    def bschu(self):
        self.listWidget.addItem("제주 흑돼지 아보카도 샌드위치 : 20000")
        variable.totalmoney += 20000

    def cm(self):
        deleteText = self.listWidget.currentItem()
        deleteText = deleteText.text()
        lista = re.findall(r'\d+', deleteText)
        variable.totalmoney -= int(lista[0])
        self.listWidget.takeItem(self.listWidget.currentRow())

    def sshow(self):
        self.pageTwo = pageTwo()
        self.pageTwo.textBrowser.append("{}원 입니다".format(variable.totalmoney))
        self.pageTwo.show()
        self.close()

app = QApplication(sys.argv)
ch = pageOne()
ch.show()
app.exec_()