import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import re

UI = 'kimbabnara.ui'

class window1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(UI, self)
        self.pushButton.clicked.connect(self.orderlist)
        self.pushButton_2.clicked.connect(self.orderlist2)
        self.pushButton_3.clicked.connect(self.orderlist3)
        self.pushButton_4.clicked.connect(self.orderlist4)
        self.listWidget.itemDoubleClicked.connect(self.orderlist_delete)
        self.pushButton_5.clicked.connect(self.calculation)
        self.price=0
        self.msg = QMessageBox()
    def orderlist(self):
        self.listWidget.addItem("된장찌개3500원")
        self.price+=3500
    def orderlist2(self):
        self.listWidget.addItem("순두부찌개4000원")
        self.price += 4000
    def orderlist3(self):
        self.listWidget.addItem("김치찌개3700")
        self.price += 3700
    def orderlist4(self):
        self.listWidget.addItem("돈가스7000")
        self.price += 7000
    def orderlist_delete(self):
        #currentRow = 선택한항목이 몇번째항목인지 반환

        deleteText = self.listWidget.currentItem()
        deleteText = deleteText.text()
        lista = re.findall(r'\d+', deleteText)
        self.price -= int(lista[0])
        self.listWidget.takeItem(self.listWidget.currentRow())

    def calculation(self):
        #메시지박스
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('MessageBox')
        self.msg.setText("{}원입니다.".format(self.price))
        self.msg.setStandardButtons(QMessageBox.Ok)
        retval=self.msg.exec_()

app = QApplication(sys.argv)
a = window1()
a.show()
app.exec_()

