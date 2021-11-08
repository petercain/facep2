import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui
import sqlite3
import datetime

page1 = "login.ui"
page2 = "join.ui"
page3 = "main.ui"
page4 = "change.ui"
page5 = "sb.ui"
page6 = "bye.ui"

class Login:
    Id = 0
    Nick = 0

class pageFive(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page5, self)

        self.kdialog.setWindowTitle("계산")
        self.kdialog.setGeometry(100,100,500,500)



        self.tabWidget.setStyleSheet("QTabBar:tab {"" height: 100px; width: 410px;"" }")
        self.label.setPixmap(QtGui.QPixmap("logo3.jpg"))
        self.label_2.setPixmap(QtGui.QPixmap("ame3.jpg"))
        self.label_5.setPixmap(QtGui.QPixmap("jamon1.jpg"))
        self.label_8.setPixmap(QtGui.QPixmap("jeju1.png"))
        self.label_11.setPixmap(QtGui.QPixmap("doll1.jpg"))
        self.label_12.setPixmap(QtGui.QPixmap("java1.jpg"))
        self.label_13.setPixmap(QtGui.QPixmap("mal3.jpg"))
        self.label_20.setPixmap(QtGui.QPixmap("ku1.jpg"))
        self.label_21.setPixmap(QtGui.QPixmap("scon1.jpg"))
        self.label_22.setPixmap(QtGui.QPixmap("mex1.jpg"))
        self.label_23.setPixmap(QtGui.QPixmap("es1.jpg"))
        self.label_24.setPixmap(QtGui.QPixmap("ds1.jpg"))
        self.label_25.setPixmap(QtGui.QPixmap("bs1.jpg"))



        self.price = 0
        self.ame = 0
        self.jamon = 0
        self.jeju = 0
        self.doll = 0
        self.java = 0
        self.mal = 0
        self.ku = 0
        self.scon = 0
        self.mex = 0
        self.es = 0
        self.ds = 0
        self.bs = 0
        self.money = 0

        self.pushButton.clicked.connect(self.change)
        self.pushButton_14.clicked.connect(self.btn_clicked_14)
        self.pushButton_15.clicked.connect(self.btn_clicked_15)
        self.pushButton_16.clicked.connect(self.btn_clicked_16)

        self.pushButton_2.clicked.connect(self.btn_clicked_2)
        self.pushButton_2.clicked.connect(self.btn_clicked_god)
        self.pushButton_2_2.clicked.connect(self.btn_clicked_2_2)
        self.pushButton_2_2.clicked.connect(self.btn_clicked_god)

        self.pushButton_3.clicked.connect(self.btn_clicked_3)
        self.pushButton_3.clicked.connect(self.btn_clicked_god)
        self.pushButton_3_3.clicked.connect(self.btn_clicked_3_3)
        self.pushButton_3_3.clicked.connect(self.btn_clicked_god)

        self.pushButton_4.clicked.connect(self.btn_clicked_4)
        self.pushButton_4.clicked.connect(self.btn_clicked_god)
        self.pushButton_4_4.clicked.connect(self.btn_clicked_4_4)
        self.pushButton_4_4.clicked.connect(self.btn_clicked_god)

        self.pushButton_5.clicked.connect(self.btn_clicked_5)
        self.pushButton_5.clicked.connect(self.btn_clicked_god)
        self.pushButton_5_5.clicked.connect(self.btn_clicked_5_5)
        self.pushButton_5_5.clicked.connect(self.btn_clicked_god)

        self.pushButton_6.clicked.connect(self.btn_clicked_6)
        self.pushButton_6.clicked.connect(self.btn_clicked_god)
        self.pushButton_6_6.clicked.connect(self.btn_clicked_6_6)
        self.pushButton_6_6.clicked.connect(self.btn_clicked_god)

        self.pushButton_7.clicked.connect(self.btn_clicked_7)
        self.pushButton_7.clicked.connect(self.btn_clicked_god)
        self.pushButton_7_7.clicked.connect(self.btn_clicked_7_7)
        self.pushButton_7_7.clicked.connect(self.btn_clicked_god)

        self.pushButton_8.clicked.connect(self.btn_clicked_8)
        self.pushButton_8.clicked.connect(self.btn_clicked_god)
        self.pushButton_8_8.clicked.connect(self.btn_clicked_8_8)
        self.pushButton_8_8.clicked.connect(self.btn_clicked_god)

        self.pushButton_9.clicked.connect(self.btn_clicked_9)
        self.pushButton_9.clicked.connect(self.btn_clicked_god)
        self.pushButton_9_9.clicked.connect(self.btn_clicked_9_9)
        self.pushButton_9_9.clicked.connect(self.btn_clicked_god)

        self.pushButton_10.clicked.connect(self.btn_clicked_10)
        self.pushButton_10.clicked.connect(self.btn_clicked_god)
        self.pushButton_10_10.clicked.connect(self.btn_clicked_10_10)
        self.pushButton_10_10.clicked.connect(self.btn_clicked_god)

        self.pushButton_11.clicked.connect(self.btn_clicked_11)
        self.pushButton_11.clicked.connect(self.btn_clicked_god)
        self.pushButton_11_11.clicked.connect(self.btn_clicked_11_11)
        self.pushButton_11_11.clicked.connect(self.btn_clicked_god)

        self.pushButton_12.clicked.connect(self.btn_clicked_12)
        self.pushButton_12.clicked.connect(self.btn_clicked_god)
        self.pushButton_12_12.clicked.connect(self.btn_clicked_12_12)
        self.pushButton_12_12.clicked.connect(self.btn_clicked_god)

        self.pushButton_13.clicked.connect(self.btn_clicked_13)
        self.pushButton_13.clicked.connect(self.btn_clicked_god)
        self.pushButton_13_13.clicked.connect(self.btn_clicked_13_13)
        self.pushButton_13_13.clicked.connect(self.btn_clicked_god)

    def btn_clicked_2(self,n):
        for i in range(n+1):
            self.ame += 1
    def btn_clicked_2_2(self,n):
        for i in range(n+1):
            self.ame -= 1
            if self.ame <= 0:
                self.ame = 0

    def btn_clicked_3(self,n):
        for i in range(n+1):
            self.jamon += 1
    def btn_clicked_3_3(self,n):
        for i in range(n+1):
            self.jamon -= 1
            if self.jamon <= 0:
                self.jamon = 0

    def btn_clicked_4(self,n):
        for i in range(n+1):
            self.jeju += 1
    def btn_clicked_4_4(self,n):
        for i in range(n+1):
            self.jeju -= 1
            if self.jeju <= 0:
                self.jeju = 0

    def btn_clicked_5(self,n):
        for i in range(n+1):
            self.doll += 1
    def btn_clicked_5_5(self,n):
        for i in range(n+1):
            self.doll -= 1
            if self.doll <= 0:
                self.doll = 0

    def btn_clicked_6(self,n):
        for i in range(n+1):
            self.java += 1
    def btn_clicked_6_6(self,n):
        for i in range(n+1):
            self.java -= 1
            if self.java <= 0:
                self.java = 0

    def btn_clicked_7(self,n):
        for i in range(n+1):
            self.mal += 1
    def btn_clicked_7_7(self,n):
        for i in range(n+1):
            self.mal -= 1
            if self.mal <= 0:
                self.mal = 0

    def btn_clicked_8(self,n):
        for i in range(n+1):
            self.ku += 1
    def btn_clicked_8_8(self,n):
        for i in range(n+1):
            self.ku -= 1
            if self.ku <= 0:
                self.ku = 0

    def btn_clicked_9(self,n):
        for i in range(n+1):
            self.scon += 1
    def btn_clicked_9_9(self,n):
        for i in range(n+1):
            self.scon -= 1
            if self.scon <= 0:
                self.scon = 0

    def btn_clicked_10(self,n):
        for i in range(n+1):
            self.mex += 1
    def btn_clicked_10_10(self,n):
        for i in range(n+1):
            self.mex -= 1
            if self.mex <= 0:
                self.mex = 0

    def btn_clicked_11(self,n):
        for i in range(n+1):
            self.es += 1
    def btn_clicked_11_11(self,n):
        for i in range(n+1):
            self.es -= 1
            if self.es <= 0:
                self.es = 0

    def btn_clicked_12(self,n):
        for i in range(n+1):
            self.ds += 1
    def btn_clicked_12_12(self,n):
        for i in range(n+1):
            self.ds -= 1
            if self.ds <= 0:
                self.ds = 0

    def btn_clicked_13(self,n):
        for i in range(n+1):
            self.bs += 1
    def btn_clicked_13_13(self,n):
        for i in range(n+1):
            self.bs -= 1
            if self.bs <= 0:
                self.bs = 0

    def btn_clicked_god(self):
        self.textBrowser.clear()
        if self.ame > 0:
            self.textBrowser.append("아메리카노 X {}".format(self.ame))
        if self.jamon > 0:
            self.textBrowser.append("허니 자몽 블랙티 X {}".format(self.jamon))
        if self.jeju > 0:
            self.textBrowser.append("제주 쑥떡 크림 프라푸치노 X {}".format(self.jeju))
        if self.doll > 0:
            self.textBrowser.append("돌체 콜드브루 X {}".format(self.doll))
        if self.java > 0:
            self.textBrowser.append("자바칩 프라푸치노 X {}".format(self.java))
        if self.mal > 0:
            self.textBrowser.append("말차 크림 프라푸치노 X {}".format(self.mal))
        if self.ku > 0:
            self.textBrowser.append("프렌치 크루와상 X {}".format(self.ku))
        if self.scon > 0:
            self.textBrowser.append("클래식 스콘 X {}".format(self.scon))
        if self.mex > 0:
            self.textBrowser.append("멕시칸 라이스 브리또 X {}".format(self.mex))
        if self.es > 0:
            self.textBrowser.append("에그에그 샌드위치 X {}".format(self.es))
        if self.ds > 0:
            self.textBrowser.append("포크 커틀릿 샌드위치 X {}".format(self.ds))
        if self.bs > 0:
            self.textBrowser.append("제주 흑돼지 아보카도 샌드위치 X {}".format(self.bs))
        self.price = self.ame*4100 + self.jamon*5800 + self.jeju*7500 + self.doll*5800 \
                     + self.java*6100 + self.mal*6300 + self.ku*3200 + self.scon*3200 + self.mex*5600 + \
                     self.es*4400 + self.ds*5900 + self.bs*6200
        if self.price > 0:
            self.textBrowser.append("총 가격은 %d원 입니다" % self.price)



    def btn_clicked_14(self):
        self.textBrowser_2.clear()
        if self.ame > 0:
            self.textBrowser_2.append("아메리카노 X {}\n".format(self.ame))
        if self.jamon > 0:
            self.textBrowser_2.append("허니 자몽 블랙티 X {}\n".format(self.jamon))
        if self.jeju > 0:
            self.textBrowser_2.append("제주 쑥떡 크림 프라푸치노 X {}\n".format(self.jeju))
        if self.doll > 0:
            self.textBrowser_2.append("돌체 콜드브루 X {}\n".format(self.doll))
        if self.java > 0:
            self.textBrowser_2.append("자바칩 프라푸치노 X {}\n".format(self.java))
        if self.mal > 0:
            self.textBrowser_2.append("말차 크림 프라푸치노 X {}\n".format(self.mal))
        if self.ku > 0:
            self.textBrowser_2.append("프렌치 크루와상 X {}\n".format(self.ku))
        if self.scon > 0:
            self.textBrowser_2.append("클래식 스콘 X {}\n".format(self.scon))
        if self.mex > 0:
            self.textBrowser_2.append("멕시칸 라이스 브리또 X {}\n".format(self.mex))
        if self.es > 0:
            self.textBrowser_2.append("에그에그 샌드위치 X {}\n".format(self.es))
        if self.ds > 0:
            self.textBrowser_2.append("포크 커틀릿 샌드위치 X {}\n".format(self.ds))
        if self.bs > 0:
            self.textBrowser_2.append("제주 흑돼지 아보카도 샌드위치 X {}\n".format(self.bs))
        self.price = self.ame * 4100 + self.jamon * 5800 + self.jeju * 7500 + self.doll * 5800 + self.java * 6100 + self.mal * 6300 + self.ku * 3200 + self.scon * 3200 + self.mex * 5600 + self.es * 4400 + self.ds * 5900 + self.bs * 6200
        if self.price > 0:
            self.textBrowser_2.append("총 가격은 %d원 입니다\n" % self.price)
        x = self.textEdit.toPlainText()

        if self.textEdit.toPlainText().isdigit() == False:
            self.textBrowser_2.append("돈 을 넣 어 주 세 요")
        else:
            self.money = self.money + int(x) # textEdit값 가져오기
            self.textBrowser_2.append("현재 투입 금액 : {}\n".format(self.money))
            self.textEdit.clear()

#현금계산 완료
    def btn_clicked_15(self):
        now = datetime.datetime.now()
        gume = []
        conn = sqlite3.connect("SBMember.db", isolation_level=None)
        cur = conn.cursor()
        if self.ame > 0:
            gume.append("아메리카노 X {}".format(self.ame))
        if self.jamon > 0:
            gume.append("허니 자몽 블랙티 X {}".format(self.jamon))
        if self.jeju > 0:
            gume.append("제주 쑥떡 크림 프라푸치노 X {}".format(self.jeju))
        if self.doll > 0:
            gume.append("돌체 콜드브루 X {}".format(self.doll))
        if self.java > 0:
            gume.append("자바칩 프라푸치노 X {}".format(self.java))
        if self.mal > 0:
            gume.append("말차 크림 프라푸치노 X {}".format(self.mal))
        if self.ku > 0:
            gume.append("프렌치 크루와상 X {}".format(self.ku))
        if self.scon > 0:
            gume.append("클래식 스콘 X {}".format(self.scon))
        if self.mex > 0:
            gume.append("멕시칸 라이스 브리또 X {}".format(self.mex))
        if self.es > 0:
            gume.append("에그에그 샌드위치 X {}".format(self.es))
        if self.ds > 0:
            gume.append("포크 커틀릿 샌드위치 X {}".format(self.ds))
        if self.bs > 0:
            gume.append("제주 흑돼지 아보카도 샌드위치 X {}".format(self.bs))

        x = " ".join(gume)

        if self.money - self.price >= 0:
            cur.execute("INSERT INTO ORDERED(ID, MENU, PRICE, TIMED)VALUES(?,?,?,?)", (Login.Id, x, self.price,now.strftime("%Y.%m.%d %H:%M:%S")))
            QMessageBox.about(self, " ", "계산이 완료되었습니다.")
            self.price = 0
            self.ame = 0
            self.jamon = 0
            self.jeju = 0
            self.doll = 0
            self.java = 0
            self.mal = 0
            self.ku = 0
            self.scon = 0
            self.mex = 0
            self.es = 0
            self.ds = 0
            self.bs = 0
            self.money = 0
            self.pageThree = pageThree()
            self.pageThree.show()
            self.kdialog.close()
            self.close()


            if self.money - self.price > 0:
                self.textBrowser_2.append("{}원을 반환합니다\n".format(self.money - self.price))


        else:
            self.textBrowser_2.append("돈이 부족합니다. 좀 더 투입해주세요")

#카드계산 완료
    def btn_clicked_16(self):
        now = datetime.datetime.now()
        gume = []
        conn = sqlite3.connect("SBMember.db", isolation_level=None)
        cur = conn.cursor()
        if self.ame > 0:
            gume.append("아메리카노 X {}".format(self.ame))
        if self.jamon > 0:
            gume.append("허니 자몽 블랙티 X {}".format(self.jamon))
        if self.jeju > 0:
            gume.append("제주 쑥떡 크림 프라푸치노 X {}".format(self.jeju))
        if self.doll > 0:
            gume.append("돌체 콜드브루 X {}".format(self.doll))
        if self.java > 0:
            gume.append("자바칩 프라푸치노 X {}".format(self.java))
        if self.mal > 0:
            gume.append("말차 크림 프라푸치노 X {}".format(self.mal))
        if self.ku > 0:
            gume.append("프렌치 크루와상 X {}".format(self.ku))
        if self.scon > 0:
            gume.append("클래식 스콘 X {}".format(self.scon))
        if self.mex > 0:
            gume.append("멕시칸 라이스 브리또 X {}".format(self.mex))
        if self.es > 0:
            gume.append("에그에그 샌드위치 X {}".format(self.es))
        if self.ds > 0:
            gume.append("포크 커틀릿 샌드위치 X {}".format(self.ds))
        if self.bs > 0:
            gume.append("제주 흑돼지 아보카도 샌드위치 X {}".format(self.bs))

        x = " ".join(gume)


        cur.execute("INSERT INTO ORDERED(ID, MENU, PRICE, TIMED)VALUES(?,?,?,?)",
                    (Login.Id, x, self.price, now.strftime("%Y.%m.%d %H:%M:%S")))
        QMessageBox.about(self, " ", "계산이 완료되었습니다.")
        self.kdialog.close()
        self.price = 0
        self.ame = 0
        self.jamon = 0
        self.jeju = 0
        self.doll = 0
        self.java = 0
        self.mal = 0
        self.ku = 0
        self.scon = 0
        self.mex = 0
        self.es = 0
        self.ds = 0
        self.bs = 0
        self.money = 0
        self.pageThree = pageThree()
        self.pageThree.show()
        self.close()



    def change(self):
        if self.price > 0:
            self.kdialog.show()
            self.textBrowser_2.clear()
            if self.ame > 0:
                self.textBrowser_2.append("아메리카노 X {}\n".format(self.ame))
            if self.jamon > 0:
                self.textBrowser_2.append("허니 자몽 블랙티 X {}\n".format(self.jamon))
            if self.jeju > 0:
                self.textBrowser_2.append("제주 쑥떡 크림 프라푸치노 X {}\n".format(self.jeju))
            if self.doll > 0:
                self.textBrowser_2.append("돌체 콜드브루 X {}\n".format(self.doll))
            if self.java > 0:
                self.textBrowser_2.append("자바칩 프라푸치노 X {}\n".format(self.java))
            if self.mal > 0:
                self.textBrowser_2.append("말차 크림 프라푸치노 X {}\n".format(self.mal))
            if self.ku > 0:
                self.textBrowser_2.append("프렌치 크루와상 X {}\n".format(self.ku))
            if self.scon > 0:
                self.textBrowser_2.append("클래식 스콘 X {}\n".format(self.scon))
            if self.mex > 0:
                self.textBrowser_2.append("멕시칸 라이스 브리또 X {}\n".format(self.mex))
            if self.es > 0:
                self.textBrowser_2.append("에그에그 샌드위치 X {}\n".format(self.es))
            if self.ds > 0:
                self.textBrowser_2.append("포크 커틀릿 샌드위치 X {}\n".format(self.ds))
            if self.bs > 0:
                self.textBrowser_2.append("제주 흑돼지 아보카도 샌드위치 X {}\n".format(self.bs))
            self.price = self.ame*4100 + self.jamon*5800 + self.jeju*7500 + self.doll*5800 + self.java*6100 + self.mal*6300 + self.ku*3200 + self.scon*3200 + self.mex*5600 + self.es*4400 + self.ds*5900 + self.bs*6200
            if self.price > 0:
                self.textBrowser_2.append("총 가격은 %d원 입니다" % self.price)

#회원탈퇴
class byep(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page6, self)

        self.label_bye.setText("{}님, 탈퇴하시겠습니까.".format(Login.Nick))

        self.pushButton_huu.clicked.connect(self.back)

        self.pushButton_TT.clicked.connect(self.byebye)

    def back(self):
        self.pageThree = pageThree()
        self.pageThree.show()
        self.close()

    def byebye(self):
        conn = sqlite3.connect("SBMember.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("DELETE FROM MEMBER WHERE ID = '{}'".format(Login.Id))
        cur.execute("DELETE FROM ORDERED WHERE ID = '{}'".format(Login.Id))
        QMessageBox.about(self, " ", "탈퇴완료.")
        self.pageOne = pageOne()
        self.pageOne.show()
        self.close()




#회원정보 수정
class pageFour(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page4, self)

        self.label_logo.setPixmap(QtGui.QPixmap("logo3.jpg"))

        self.label_ID.setText(Login.Id)

        self.textEdit_nick_c.setText(Login.Nick)

        self.pushButton_change.clicked.connect(self.changep)

    def changep(self):
        if len(self.textEdit_nick_c.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "닉네임이 너무 짧습니다.")
        elif len(self.textEdit_pass2_c.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "비밀번호가 너무 짧습니다.")
        elif self.textEdit_pass2_c.toPlainText() != self.textEdit_pass2r_c.toPlainText():
            QMessageBox.critical(self, " ", "입력한 비밀번호와 재입력한 비밀번호가 일치하지 않습니다. 다시 확인해 주세요.")

        else:
            conn = sqlite3.connect("SBMember.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("UPDATE MEMBER SET NICKNAME = '{}' WHERE ID = '{}'".format(self.textEdit_nick_c.toPlainText(), Login.Id))
            cur.execute("UPDATE MEMBER SET PASS = '{}' WHERE ID = '{}'".format(self.textEdit_pass2r_c.toPlainText(), Login.Id))
            cur.execute("SELECT NICKNAME FROM MEMBER WHERE ID = '{}'".format(Login.Id))
            result = cur.fetchall()
            x = result[0]
            Login.Nick = x[0]
            QMessageBox.about(self, " ", "회원정보 변경이 완료 되었습니다.")
            self.pageThree = pageThree()
            self.pageThree.show()
            self.close()





#주문내역확인과 회원정보수정, 주문하러가기
class pageThree(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page3, self)

        self.label_logo.setPixmap(QtGui.QPixmap("logo3.jpg"))

        self.label_hi.setText("{}님, 안녕하세요. 스타벅스입니다.".format(Login.Nick))

        self.pushButton_jumoon.clicked.connect(self.jumon)

        self.pushButton_change_m.clicked.connect(self.changem)

        self.pushButton_gume.clicked.connect(self.gume)

        self.pushButton_bye.clicked.connect(self.bye)



    def jumon(self):
        self.pageFive = pageFive()
        self.pageFive.show()
        self.close()

    def changem(self):
        self.pageFour = pageFour()
        self.pageFour.show()
        self.close()

    def gume(self):
        self.textBrowser_g.clear()
        conn = sqlite3.connect("SBMember.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT * FROM ORDERED WHERE ID = '{}'".format(Login.Id))
        result = cur.fetchall()
        for i in range(len(result)):
            a = result[i][1]
            b = result[i][2]
            c = result[i][3]
            self.textBrowser_g.append("구매목록 : {}\n구매가격 : {}원\n구매시간 : {}\n".format(a,b,c))

    def bye(self):
        self.byep = byep()
        self.byep.show()
        self.close()


#회원가입
class pageTwo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page2, self)

        self.label_logo.setPixmap(QtGui.QPixmap("logo3.jpg"))

        self.pushButton_join2.clicked.connect(self.good)


    def good(self):
        che_list = []
        conn = sqlite3.connect("SBMember.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT ID FROM MEMBER")
        result = cur.fetchall()
        for row in result:
            che_list.append(row[0])
        if len(self.textEdit_id2.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "아이디가 너무 짧습니다.")
        elif self.textEdit_id2.toPlainText() in che_list:
            QMessageBox.critical(self, " ", "이미 존재하는 아이디입니다.")
        elif len(self.textEdit_nick.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "닉네임이 너무 짧습니다.")
        elif len(self.textEdit_pass2.toPlainText()) == 0:
            QMessageBox.critical(self, " ", "비밀번호가 너무 짧습니다.")
        elif self.textEdit_pass2.toPlainText() != self.textEdit_pass2r.toPlainText():
            QMessageBox.critical(self, " ", "입력한 비밀번호와 재입력한 비밀번호가 일치하지 않습니다. 다시 확인해 주세요.")


        else:
            cur.execute("INSERT INTO MEMBER(ID, PASS, NICKNAME)values(?,?,?)",(self.textEdit_id2.toPlainText(),self.textEdit_pass2r.toPlainText(),self.textEdit_nick.toPlainText()))
            self.pageOne = pageOne()
            self.pageOne.show()
            self.close()


#첫 페이지, 로그인과 회원가입 버튼
class pageOne(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi(page1, self)

        self.label_logo.setPixmap(QtGui.QPixmap("logo3.jpg"))

        self.pushButton_join.clicked.connect(self.mjoin)

        self.pushButton_login.clicked.connect(self.login)

    def mjoin(self):
        self.pageTwo = pageTwo()
        self.pageTwo.show()
        self.close()

    def login(self):
        try:
            conn = sqlite3.connect("SBMember.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("SELECT PASS FROM MEMBER WHERE ID = '{}'".format(self.textEdit_id.toPlainText()))
            result = cur.fetchall()
            x = result[0]
            if x[0] == self.textEdit_pass.toPlainText():
                cur.execute("SELECT NICKNAME FROM MEMBER WHERE ID = '{}'".format(self.textEdit_id.toPlainText()))
                result = cur.fetchall()
                x = result[0]
                Login.Nick = x[0]
                Login.Id = self.textEdit_id.toPlainText()
                self.pageThree = pageThree()
                self.pageThree.show()
                self.close()
            else:
                QMessageBox.critical(self, " ", "비밀번호가 틀렸습니다.")
        except:
            QMessageBox.critical(self, " ", "존재하지 않는 아이디입니다.")




app = QApplication(sys.argv)
bs = pageOne()
bs.show()
app.exec_()