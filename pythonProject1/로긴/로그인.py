import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
import sqlite3

one = '로그인창.ui'
two = '회원가입창.ui'


class window2(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(two, self)

        self.pushButton_3.clicked.connect(self.good)

    def good(self):
        che_list = []
        conn = sqlite3.connect("logins.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM login")
        result = cur.fetchall()
        for row in result:
            che_list.append(row[0])
        if self.textEdit_3.toPlainText() in che_list:
            QMessageBox.critical(self, " ", "이미 존재하는 아이디입니다.")
        elif len(self.textEdit_4.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "비밀번호가 너무 짧습니다.")

        else:
            lp = (
                ('{}'.format(self.textEdit_3.toPlainText()), '{}'.format(self.textEdit_4.toPlainText()))
            )
            ins = "INSERT INTO login(id, pass)values(?,?)"
            cur.execute(ins, lp)
            conn.commit()
            self.window1 = window1()
            self.window1.show()
            self.close()

class window1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi(one, self)

        self.pushButton.clicked.connect(self.join)

        self.pushButton_2.clicked.connect(self.login)

    def join(self):
        self.window2 = window2()
        self.window2.show()
        self.close()

    def login(self):
        try:
            conn = sqlite3.connect("logins.db")
            cur = conn.cursor()
            cur.execute("SELECT pass FROM login WHERE id = '{}'".format(self.textEdit.toPlainText()))
            result = cur.fetchall()
            x = result[0]
            if x[0] == self.textEdit_2.toPlainText():
                QMessageBox.about(self, " ", "로그인 성공")
            else:
                QMessageBox.critical(self, " ", "비밀번호가 틀렸습니다.")
        except:
            QMessageBox.critical(self, " ", "존재하지 않는 아이디입니다.")

app = QApplication(sys.argv)
ss = window1()
ss.show()
app.exec_()