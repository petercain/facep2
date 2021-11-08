import sys,pymysql
from random import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic  # ui 불러오기 위해 필요
from PyQt5 import QtWidgets  # 이게 있어야 아래 정렬 함수가 제대로 활성화된다!!
import pyautogui
import sqlite3
import time
import datetime
import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

#폴더명 경로안에 있을때 자동으로 불러오기
page1 = uic.loadUiType("../starDB/first.ui")[0]
page2 = uic.loadUiType("../starDB/second.ui")[0]

class MainWindow(QMainWindow, page1):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.PassWord.textEdited.connect(self.error) # PassWord 에러 메세지
        self.ID.textEdited.connect(self.errorfunction) # ID 에러 메세지
        self.loginbtn.clicked.connect(self.loginfunction) # 로그인 하기

    def loginfunction(self): # 로그인
        if self.PassWord.text() == "1234" and self.ID.text() == "starDB":
            self.page2 = LoadWindow()
            self.page2.show()
            self.close()

    def errorfunction(self): # ID에러 메세지
        ID = self.ID.text()
        if ID != "starDB":
            self.t_2.setText("아이디를 바르게 입력해주세요.")
            self.t_2.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(239, 41, 41);}""")
            self.PassWord.setStyleSheet("""
                  QLineEdit{border:0px; border-bottom: 2px outset; border-color: rgb(239, 41, 41); padding-left: 10px;}            
                  """)
        else:
            self.t_2.setText(" ")
            self.t_2.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(78, 154, 6);}""")
            self.PassWord.setStyleSheet("""
                QLineEdit {border:0px; border-bottom: 2px outset; border-color: rgb(0, 112, 74); padding-left: 10px;}
                """)
    def error(self): # 비밀번호 에러 메세지
        PassWord = self.PassWord.text()
        if PassWord == "1234":
            self.t.setText("로그인 버튼을 눌러주세요.")
            self.t.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(78, 154, 6);}""")
            self.PassWord.setStyleSheet("""
            QLineEdit {border:0px; border-bottom: 2px outset; border-color: rgb(0, 112, 74); padding-left: 10px;}
            """)
        else :
            self.t.setText("비밀번호가 일치하지 않습니다.")
            self.t.setStyleSheet("""QLabel {font: 75 italic 11pt "Ubuntu Mono"; color: rgb(239, 41, 41);}""")
            self.PassWord.setStyleSheet("""
            QLineEdit{border:0px; border-bottom: 2px outset; border-color: rgb(239, 41, 41); padding-left: 10px;}            
            """)

class LoadWindow(QMainWindow, page2):  #ui1
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.loadbtn1.clicked.connect(self.loadfunction) # 지점명 등록 조회 (중복확인)
        self.joinbtn1.clicked.connect(self.joinfunction) # 지점 등록
        self.changebtn1.clicked.connect(self.changefunction) # 지점 정보 변경
        self.deletebtn1.clicked.connect(self.deletefunction) # 지점 삭제
        self.loadbtn3.clicked.connect(self.BranchSalesranking) # 지점별 매출 순위 조회
        self.logoutbtn.clicked.connect(self.logoutfunction)  # 로그아웃

        self.loadbtn4.clicked.connect(self.gload) #총 매출 조회

        # FigureCanvas() 그림을 그릴 영역을 나타내는 객체
        # QVBoxLayou 위젯을 수평으로 정령하는 레이아웃 클래스
        # addWidget 위젯을 추가하는 메서드
        # canvas를 그림을 그릴 객체로 만들고 vbox는 위젯을 수평으로 정렬한 것. 거기에 그림 그릴 객체 추가
        # matplotlib은 한 번에 한장의 그림을 그린다. 이 그림을 가리키는 용어가 figure이다.
        # subplots()은 그래프의 기본 프레임 같은것. 이 gui에서 처음 그래프 보이는 부분
        canvas = FigureCanvas()
        vbox = QVBoxLayout(self.widget_2)
        vbox.addWidget(canvas)
        self.ax = canvas.figure.subplots()

        # self.comboBox_list_6.setEditable(True) # 콤보박스에 Edit 씌우기
        # self.comboBox_list_6.lineEdit().setAlignment(Qt.AlignCenter) # LineEdit 가운데 정렬
        # self.comboBox_list_6.lineEdit().setReadOnly(True) # LineEdit 읽기모드 설정
        # self.comboBox_list_6.lineEdit().setStyleSheet("QLineEdit{border-radius: 7px;}") # LineEdit 테두리 둥글게 하기

        # global Branch_name1
        # Branch_name1 = self.Branch_name1.text()
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT Branch_name FROM Head")
        result = cur.fetchall()
        print(result)

        for i in result:
            print(type(i))
            i[1:]
            print(i)
            self.Brandch_name2.addItem("{}".format(i))


    def loadfunction(self): # 지점명 등록 조회
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
        cur = conn.cursor()
        Branch_name1 = self.Branch_name1.text()
        cur.execute("SELECT * FROM Head WHERE Branch_name = '{}'".format(Branch_name1))
        result = cur.fetchone()
        if not result:
            QMessageBox.information(self, '성공', "등록가능합니다.", QMessageBox.Yes)
            self.Branch_address1.clear()
            self.Branch_owner1.clear()
            self.Branch_hp1.clear()
        else:
            self.Branch_address1.setText("{}".format(result[1]))
            self.Branch_owner1.setText("{}".format(result[2]))
            self.Branch_hp1.setText("{}".format(result[3]))


    def joinfunction(self): # 지점 등록
        global Branch_name1
        Branch_name1 = self.Branch_name1.text()
        Branch_address1 = self.Branch_address1.text()
        Branch_owner1 = self.Branch_owner1.text()
        Branch_hp1 = self.Branch_hp1.text()
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
        cur = conn.cursor()
        Branch_name1 = self.Branch_name1.text()
        cur.execute("SELECT Branch_name FROM Head WHERE Branch_name = '{}'".format(Branch_name1))
        result = cur.fetchone()
        if Branch_name1 == "":
            QMessageBox.information(
                self, '오류', "아이디를 입력해주세요", QMessageBox.Yes)
        elif result:
            QMessageBox.information(
                self, '오류', "이미 등록된 지점입니다", QMessageBox.Yes)
        elif Branch_address1 == "":
            QMessageBox.information(
                self, '오류', "지점위치를 입력해주세요", QMessageBox.Yes)
        elif Branch_owner1 == "":
            QMessageBox.information(
                self, '오류', "점주명를 입력해주세요", QMessageBox.Yes)
        elif Branch_hp1 == "":
            QMessageBox.information(
                self, '오류', "전화번호를 입력해주세요", QMessageBox.Yes)
        else:
            conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
            cur = conn.cursor()
            now = (('{}'.format(Branch_name1), '{}'.format(Branch_address1), '{}'.format(Branch_owner1),
                    '{}'.format(Branch_hp1)))
            act = "INSERT INTO Head(Branch_name,Branch_address,Branch_owner,Branch_hp)VALUES(?,?,?,?)"
            cur.execute(act, now)

            aa = QMessageBox.information(
                self, '성공', "지점등록이 완료되었습니다.", QMessageBox.Yes)
            if aa == QMessageBox.Yes:
                self.Branch_name1.clear()
                self.Branch_address1.clear()
                self.Branch_owner1.clear()
                self.Branch_hp1.clear()
            # self.Brandch_name2.addItem('{}'.format(Branch_name1))


    def changefunction(self): # 지점 정보 변경
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)
        cur = conn.cursor()
        Branch_name1 = self.Branch_name1.text()
        Branch_address1 = self.Branch_address1.text()
        Branch_owner1 = self.Branch_owner1.text()
        Branch_hp1 = self.Branch_hp1.text()
        act = "UPDATE Head SET Branch_address = '{}'," \
              " Branch_owner='{}',Branch_hp='{}' WHERE Branch_name = '{}'".format(Branch_address1, Branch_owner1,
                                                                                  Branch_hp1, Branch_name1)
        cur.execute(act)
        QMessageBox.information(
            self, '확인', "정보가 변경되었습니다", QMessageBox.Yes)


    def deletefunction(self): # 지점 삭제
        reset = pyautogui.confirm("정말 지점을 삭제하시겠습니까?",'경고',
                              ["예","아니요"])
        if reset == "예" :
            conn = sqlite3.connect("Star_Bucks.db",isolation_level=None)
            cur = conn.cursor()
            cur.execute("DELETE FROM Head WHERE Branch_name = '{}'".format(Branch_name1))
            self.Branch_name1.clear()
            self.Branch_address1.clear()
            self.Branch_owner1.clear()
            self.Branch_hp1.clear()
            # delete = self.Brandch_name2.currentText()
            # self.Brandch_name2.removeItem(delete)


    def BranchSalesranking(self): # 지점별 매출 순위
        year = self.comboBox_list_9.currentText()
        month = self.comboBox_list_8.currentText()
        day = self.comboBox_list_7.currentText()
        print(year, month, day)
        conn = sqlite3.connect("Star_Bucks.db", isolation_level=None) # 오토커밋
        cur = conn.cursor() # 커서 설정
        # sql문으로 db에 저장된 값 불러오기
        Total_Money_day = """
        SELECT Branch_name, Day, Price FROM order_data WHERE Day = "{}-{}-{}" GROUP BY Branch_name ORDER BY Day
        """
        cur.execute(Total_Money_day.format(year, month, day))
        result = cur.fetchall()
        self.rank.addItem(" 지점     \t날짜              \t매출")
        for row in result:
            self.rank.addItem("{}  \t{}\t  {}".format(row[0],row[1],row[2]))

    def gload(self):
        peter = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                             db='starDB', charset='utf8')
        dorothy = peter.cursor()

        print("굿")
        Y = self.comboBox_list_4.currentText()
        M = self.comboBox_list_5.currentText()

        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']
        money = []


        for D in dayday:
            dorothy.execute("SELECT sum(Price)FROM Order_data WHERE Day like'{}-{}-{}'".format(Y,M,D))
            result = dorothy.fetchall()
            money.append(result[0][0])


        BabyDataset = list(zip(dayday, money))

        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        print(df)

        x = df['day']
        y = df['money']


        self.ax.clear()
        self.ax.plot(x, y, '-')
        self.ax.figure.canvas.draw()

        peter.commit()
        peter.close()


    def logoutfunction(self): # 로그아웃
        self.page1 = MainWindow()
        self.page1.show()
        self.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MainWindow()
    MainWindow.show()
    app.exec_()
