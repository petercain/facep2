import sys
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3


pageOneUi = 'kosk.ui'
pageTwoUi = 'chage.ui'


class pageTwo(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageTwoUi, self)

        self.pushButton_4.clicked.connect(self.cchage)

        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()

    def cchage(self):
        self.cur.execute("SELECT * FROM employee_data")
        X = self.cur.fetchall()
        print(X)
        self.textBrowser.append("{}".format(X))


class pageOne(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageOneUi, self)


        self.pushButton.clicked.connect(self.amechu)
        self.pushButton_3.clicked.connect(self.sshow)

        self.pushButton_2.clicked.connect(self.sshow2)

        self.conn = sqlite3.connect("data.db")
        self.cur = self.conn.cursor()
        # self.conn.execute('CREATE TABLE employee_data(id INTEGER)')
        #
        #
        # self.conn.commit()
        # self.conn.close()


    def amechu(self):
        self.conn.execute("INSERT INTO employee_data(id)values(2)")
        self.conn.commit()


    def sshow(self):
        self.cur.execute("SELECT * FROM employee_data")
        X = self.cur.fetchall()
        print(X)
        self.listWidget.addItem("{}".format(X))

    def sshow2(self):
        self.pageTwo = pageTwo()
        self.cur.execute("SELECT * FROM employee_data")
        X = self.cur.fetchall()
        print(X)
        self.pageTwo.textBrowser.append("{}".format(X))
        self.pageTwo.show()
        self.close()


app = QApplication(sys.argv)
ch = pageOne()
ch.show()
app.exec_()