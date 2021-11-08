import sys
from random import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5 import uic  # ui 불러오기 위해 필요
from PyQt5 import QtWidgets  # 이게 있어야 아래 정렬 함수가 제대로 활성화된다!!
import pyautogui
import sqlite3
import time
import datetime

#######################
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas





#폴더명 경로안에 있을때 자동으로 불러오기
page1 = uic.loadUiType("../starDB12/first.ui")[0]
page2 = uic.loadUiType("../starDB12/second.ui")[0]

class MainWindow(QMainWindow, page1):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PassWord.textEdited.connect(self.error)
        self.ID.textEdited.connect(self.errorfunction)
        self.loginbtn.clicked.connect(self.loginfunction)

    def loginfunction(self):
        # if self.PassWord.text() == "1234" and self.ID.text() == "starDB":
            self.page2 = LoadWindow()
            self.page2.show()
            self.close()

    def errorfunction(self):
        ID = self.ID.text()
        if ID != "starDB":
            self.t_2.setText("아이디를 바르게 입력해주세요.")
            self.t_2.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(239, 41, 41);}""")
            self.PassWord.setStyleSheet("""
                  QLineEdit{border:0px; border-bottom: 2px outset; border-color: rgb(239, 41, 41); padding-left: 10px;}            
                  """)
        else:
            #self.t.clear()
            self.t_2.setText(" ")
            self.t_2.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(78, 154, 6);}""")
            self.PassWord.setStyleSheet("""
                QLineEdit {border:0px; border-bottom: 2px outset; border-color: rgb(0, 112, 74); padding-left: 10px;}
                """)
    def error(self):
        PassWord = self.PassWord.text()
        if PassWord == "1234":
            self.t.setText("로그인 버튼을 눌러주세요.")
            self.t.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(78, 154, 6);}""")
            self.PassWord.setStyleSheet("""
            QLineEdit {border:0px; border-bottom: 2px outset; border-color: rgb(0, 112, 74); padding-left: 10px;}
            """)
        else :
            #self.t.clear()
            self.t.setText("비밀번호가 일치하지 않습니다.")
            self.t.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(239, 41, 41);}""")
            self.PassWord.setStyleSheet("""
            QLineEdit{border:0px; border-bottom: 2px outset; border-color: rgb(239, 41, 41); padding-left: 10px;}            
            """)

class LoadWindow(QMainWindow, page2):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logoutbtn.clicked.connect(self.logoutfunction)
        self.loadbtn1.clicked.connect(self.loadfunction)

        self.loadbtn4.clicked.connect(self.gload)

        canvas = FigureCanvas()
        vbox = QVBoxLayout(self.widget_2)
        vbox.addWidget(canvas)
        self.ax = canvas.figure.subplots()








    #     self.joinbtn1.clicked.connect(self.joinfunction)
    #
    # def joinfunction(self):
    #     conn = sqlite3.connect("Star_Bucks.db",isolation_level=None)
    #     cur = conn.cursor()
    #     ID = self.ID.toPlainText()
    #     Nickname = self.Nickname.toPlainText()
    #     PassWord = self.PassWord.toPlainText()
    #     Shop = self.Shop.toPlainText()
    #     now = (('{}'.format(ID),'{}'.format(Nickname),'{}'.format(PassWord),'{}'.format(Shop)))
    #     act = "INSERT INTO join_data(ID,Nickname,PassWord,Shop)VALUES(?,?,?,?)"
    #     cur.execute(act, now)
    #
    #     conn.commit()
    #     conn.close()
    #
    #     aa = QMessageBox.information(
    #         self, '성공', "회원가입이 완료되었습니다\n로그인을 해주세요", QMessageBox.Yes)
    #     if aa == QMessageBox.Yes:
    def loadfunction(self):
        conn = sqlite3.connect("Star_Bucks.db",isolation_level=None)
        cur = conn.cursor()
        Branch_name1 = self.Branch_name1.text()
        cur.execute("SELECT * FROM Head WHERE Branch_name = '{}'".format(Branch_name1))
        result = cur.fetchone()
        conn.commit()
        conn.close()
        self.Branch_address1.setText("{}".format(result[1]))
        self.Branch_owner1.setText("{}".format(result[2]))
        self.Branch_hp1.setText("{}".format(result[3]))

    def logoutfunction(self):
        self.page1 = MainWindow()
        self.page1.show()
        self.close()

    #방법 1) 년도를 고르면 월별 매출 조회
    #방법 2) 년도와 월을 고르면 일별 매출 조회
    #방법 3) 년도와 월을 고르면 주마다 조회(01~07,08~14,15~22,23~29, 30일이랑 31일은???)

    def gload(self):
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
        cur = conn.cursor()

        print("굿")
        Y = self.comboBox_list_4.currentText()
        M = self.comboBox_list_5.currentText()

        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        money = []


        for D in dayday:
            cur.execute("SELECT sum(Price)FROM order_data WHERE Day like'{}-{}-{}'".format(Y,M,D))
            result = cur.fetchall()
            money.append(result[0][0])

        BabyDataset = list(zip(dayday, money))

        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        print(df)

        y = df['money']
        x = df['day']


        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.figure.canvas.draw()
















if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
