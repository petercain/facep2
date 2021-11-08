import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtGui

form_class = uic.loadUiType("sb.ui")[0]
class MyWindow(QMainWindow, form_class):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.tabWidget.setStyleSheet("QTabBar:tab {"" height: 100px; width: 410px;"" }")  # 탭 크기 조정
        self.label.setPixmap(QtGui.QPixmap("logo3.jpg"))  # 라벨에 사진삽입
        self.label_2.setPixmap(QtGui.QPixmap("ame3.jpg"))
        self.label_5.setPixmap(QtGui.QPixmap("jamon1.jpg"))
        self.label_8.setPixmap(QtGui.QPixmap("jeju1.jpg"))
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

        # self.pushButton.clicked.connect(self.btn_clicked_1) #버튼에 함수주기
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
        if self.price == 0:
            self.kdialog.close()
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

        if self.textEdit.toPlainText().isdigit() == False:
            self.textBrowser_2.append("돈 을 넣 어 주 세 요")
        else:
            self.money = self.money + int(self.textEdit.toPlainText())
            self.textBrowser_2.append("현재 투입 금액 : {}\n".format(self.money))
            self.textEdit.clear()

    def btn_clicked_15(self):
        if self.price == 0:
            self.kdialog.close()
        if self.money - self.price >= 0:
            self.textBrowser_2.append("계산이 완료되었습니다\n")
            if self.money - self.price > 0:
                self.textBrowser_2.append("{}원을 반환합니다\n".format(self.money - self.price))
            self.textBrowser_2.append("\n\n====================================\n\t  즐거운하루되세요~\n====================================")
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
            self.textBrowser.clear()

        elif self.money - self.price < 0:
            self.textBrowser_2.append("돈이 부족합니다. 좀 더 투입해주세요")


    def btn_clicked_16(self):
        if self.price == 0:
            self.kdialog.close()
        self.textBrowser_2.append("\n계산이 완료되었습니다\n")

        self.textBrowser_2.append("\n\n====================================\n\t  즐거운하루되세요~\n====================================")
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
        self.textBrowser.clear()



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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()