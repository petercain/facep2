import sys
import re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3


pageOneUi = 'kosk.ui'
pageTwoUi = 'chage.ui'

class DB:
    conn = sqlite3.connect("data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM employee_data")
    X = cur.fetchall()


class pageTwo(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageTwoUi, self)

        self.pushButton_4.clicked.connect(self.cchage)

    def cchage(self):
        print(DB.X)
        self.textBrowser.append("{}".format(DB.X))


class pageOne(QDialog):

    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(pageOneUi, self)


        self.pushButton.clicked.connect(self.amechu)
        self.pushButton_3.clicked.connect(self.sshow)

        self.pushButton_2.clicked.connect(self.sshow2)

        # self.conn.execute('CREATE TABLE employee_data(id INTEGER)')
        #
        #
        # self.conn.commit()
        # self.conn.close()


    def amechu(self):
        DB.conn.execute("INSERT INTO employee_data(id)values(2)")
        DB.conn.commit()
        DB.conn.close()


    def sshow(self):
        print(DB.X)
        self.listWidget.addItem("{}".format(DB.X))

    def sshow2(self):
        self.pageTwo = pageTwo()
        self.pageTwo.show()
        self.close()


app = QApplication(sys.argv)
ch = pageOne()
ch.show()
app.exec_()