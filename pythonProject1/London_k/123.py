import sys,pymysql  # sys모듈을 가져옴
import sqlite3
import pyautogui
from PyQt5 import uic  # pytq5의 모듈에서 uic를 가져옴
from PyQt5.QtWidgets import *
import time


#qt designer로 만든 파일을 파이썬 코드로 불러올수있음

form_class = uic.loadUiType("london.ui")[0]
class MyWindow(QMainWindow,form_class): #클래스로 정의하며 밑에 다양한 함수들과 변수들을 정의

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.msg = QMessageBox()
        self.americano1 = 0
        self.latte1 = 0
        self.caramel1 = 0
        self.moca1 = 0
        self.hazel1 = 0
        self.cappu1 = 0
        self.total1 = 0
        self.add_ice1 = 0
        self.menu_list2.clear()
        # self.menu_list4.clear()

        self.login.clicked.connect(self.btn_login)  # self.버튼이름.이벤트(clicked).connect(함수불러오기)
        self.logout.clicked.connect(self.btn_logout)
        self.payment.clicked.connect(self.btn_pay)
        self.join.clicked.connect(self.btn_join)
        self.join2.clicked.connect(self.btn_join2)
        self.my.clicked.connect(self.btn_my)
        # self.my.clicked.connect(self.pm)
        self.pushButton_next.clicked.connect(self.btn_next)
        self.id_dc.clicked.connect(self.btn_id_dc)
        self.nik_dc.clicked.connect(self.btn_nik_dc)
        self.nik_dc2.clicked.connect(self.btn_nik_dc2)
        # self.up.clicked.connect(self.btn_up)
        # self.pushButton_del.clicked.connect(self.btn_del)



        self.back.clicked.connect(self.btn_back)
        self.back2.clicked.connect(self.btn_back2)
        self.back3.clicked.connect(self.btn_back3)
        self.back4.clicked.connect(self.btn_back4)


        self.cancel.clicked.connect(self.can)
        # self.cashon.clicked.connect(self.total)
        self.cash_payment.clicked.connect(self.cash)
        # self.cash_payment.clicked.connect(self.dblist)


        # self.add_ice.clicked.connect(self.addice)
        # self.add_ice.clicked.connect(self.btn_clicked_ice)
        # self.add_ice.clicked.connect(self.btn_clicked_add)

        self.americano.clicked.connect(self.btn_clicked_1)
        self.americano.clicked.connect(self.btn_text1)
        self.americano.clicked.connect(self.btn_clicked_add)

        self.latte.clicked.connect(self.btn_clicked_2)
        self.latte.clicked.connect(self.btn_text2)
        self.latte.clicked.connect(self.btn_clicked_add)

        self.caramel.clicked.connect(self.btn_clicked_3)
        self.caramel.clicked.connect(self.btn_text3)
        self.caramel.clicked.connect(self.btn_clicked_add)

        self.moca.clicked.connect(self.btn_clicked_4)
        self.moca.clicked.connect(self.btn_text4)
        self.moca.clicked.connect(self.btn_clicked_add)

        self.hazel.clicked.connect(self.btn_clicked_5)
        self.hazel.clicked.connect(self.btn_text5)
        self.hazel.clicked.connect(self.btn_clicked_add)

        self.cappu.clicked.connect(self.btn_clicked_6)
        self.cappu.clicked.connect(self.btn_text6)
        self.cappu.clicked.connect(self.btn_clicked_add)

        self.idcheck = False
        self.nikcheck = False
        self.nikcheck2 = False

        self.id_txt.textChanged.connect(self.txtchanged)
        self.nik_txt.textChanged.connect(self.txtchanged2)
        self.nik_txt2.textChanged.connect(self.txtchanged3)

    def txtchanged(self):
        self.idcheck = False

    def txtchanged2(self):
        self.nikcheck = False

    def txtchanged3(self):
        self.nikcheck2 = False

    # def btn_del(self):
    #     remove = pyautogui.confirm("정말로 탈퇴하시겠습니까?")
    #     if remove == "확인":
    #         QMessageBox.information(self, 'Exit', "탈퇴되었습니다.", QMessageBox.Yes)
    #         conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)  # 오토커밋 db연동
    #         cur = conn.cursor()  # connection으로부터 cursor생성
    #         del_id = self.up_id.text()
    #         cur.execute("DELETE FROM join_data WHERE ID = '{}'".format(del_id))
    #         result = cur.fetchone()
    #         print(result)
    #         currentpage = myWindow.stackedWidget.currentIndex()
    #         myWindow.stackedWidget.setCurrentIndex(currentpage - 5)
    #
    #     else:
    #         return

    def btn_id_dc(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        cur = conn.cursor()  # connection으로부터 cursor생성
        # 입력받은 id 변수에 저장하기
        pr_id = self.id_txt.text()
        if len(pr_id) < 4:
            QMessageBox.information(self, '오류', "4글자 이상 입력해주세요.", QMessageBox.Yes)
            self.id_txt.setText("")

        else:
            print(pr_id)
            # 중복확인
            cur.execute("SELECT ID FROM join_data WHERE ID = '{}'".format(pr_id))
            result = cur.fetchone()
            print(result)
            print(type(result))

            if result is None:
                QMessageBox.information(self, '성공', "사용가능한 아이디입니다.", QMessageBox.Yes)
                self.idcheck = True

            else:
                QMessageBox.information(self, '오류', "이미 사용중인 아이디입니다.", QMessageBox.Yes)
                self.id_txt.setText("")
                self.idcheck = False
        conn.commit()
        conn.close()

    def btn_nik_dc(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        cur = conn.cursor() # connection으로부터 cursor생성

        pr_nik = self.nik_txt.text()
        if len(pr_nik) < 1:
            QMessageBox.information(self, '오류', "닉네임 1글자 이상 입력해주세요.", QMessageBox.Yes)
            self.nik_txt.setText("")

        else:
            print(pr_nik)
            # 입력받은 id 변수에 저장하기

            # 중복확인
            cur.execute("SELECT ID FROM join_data WHERE N_name = '{}'".format(pr_nik))
            result = cur.fetchone()

            if result is None:
                QMessageBox.information(self, '성공', "사용가능한 닉네임입니다.", QMessageBox.Yes)
                self.nikcheck = True

            else:
                QMessageBox.information(self, '오류', "이미 사용중인 닉네임입니다.", QMessageBox.Yes)
                self.nik_txt.setText("")
                self.nikcheck = False

        conn.commit()
        conn.close()

    def btn_nik_dc2(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        cur = conn.cursor()  # connection으로부터 cursor생성
        pr_nik = self.nik_txt2.toPlainText()
        if len(pr_nik) < 1:
            QMessageBox.information(self, '오류', "닉네임 1글자 이상 입력해주세요.", QMessageBox.Yes)
            # self.nik_txt.setText("")

        else:
            print(pr_nik)
            # 입력받은 id 변수에 저장하기

            # 중복확인
            cur.execute("SELECT ID FROM join_data WHERE N_name = '{}'".format(pr_nik))
            result = cur.fetchone()

            if result is None or self.d:
                QMessageBox.information(self, '성공', "사용가능한 닉네임입니다.", QMessageBox.Yes)
                self.nikcheck2 = True

            else :
                QMessageBox.information(self, '오류', "이미 사용중인 닉네임입니다.", QMessageBox.Yes)
                self.nik_txt.setText("")
                self.nikcheck2 = False
        conn.commit()
        conn.close()

    def btn_login(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        cur = conn.cursor()  # connection으로부터 cursor생성
        self.lg_id = self.login_id_txt.text()
        lg_pw = self.login_pass_txt.text()

        cur.execute("SELECT ID FROM join_data WHERE ID = '{}' and PASS = '{}'".format(self.lg_id, lg_pw))
        result = cur.fetchone()

        if len(self.lg_id) < 1 and len(lg_pw) < 1:
            QMessageBox.information(self, '오류', "아이디 혹은 비밀번호를 입력해주세요.", QMessageBox.Yes)

        else:
            if result is None:
                QMessageBox.information(self, '오류', "아이디 혹은 비밀번호가 일치하지 않습니다..", QMessageBox.Yes)
                self.login_id_txt.setText("")
                self.login_pass_txt.setText("")

            else:
                currentpage = myWindow.stackedWidget.currentIndex()
                myWindow.stackedWidget.setCurrentIndex(currentpage + 2)
        conn.commit()
        conn.close()

    def btn_logout(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage - 2)
        self.login_id_txt.setText("")
        self.login_pass_txt.setText("")
        self.login_id_txt2.clear()
        self.menu_list1.clear()
        self.menu_list2.clear()

    def btn_pay(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage + 1)
        self.txt_total.append("총 가격은 {}원 입니다".format(self.total1))

    def btn_join(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage + 1)
        self.login_id_txt.setText("")
        self.login_pass_txt.setText("")


    def btn_join2(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        cur = conn.cursor()  # connection으로부터 cursor생성
        # 입력받은 id 변수에 저장하기
        pr_id = self.id_txt.text()
        pr_nik = self.nik_txt.text()
        pr_pass = self.pass_txt.text()
        pr_pass2 = self.pass2_txt.text()

        if not self.idcheck:
            QMessageBox.information(self, '오류', "아이디 중복확인을 해주세요.", QMessageBox.Yes)

            return

        if not self.nikcheck:
            QMessageBox.information(self, '오류', "닉네임 중복확인을 주세요.", QMessageBox.Yes)

            return

        if len(pr_pass) < 4 and len(pr_pass2) < 4:
            QMessageBox.information(self, '오류', "비밀번호를 4글자 이상 입력해주세요.", QMessageBox.Yes)
            self.pass_txt.setText("")
            self.pass2_txt.setText("")

        else:
            if pr_pass == pr_pass2:
                cur.execute("INSERT INTO join_data VALUES('{}','{}','{}')".format(pr_id, pr_pass, pr_nik))

                QMessageBox.information(self, '성공', "회원가입이 완료되었습니다.\n 로그인창으로 이동합니다.", QMessageBox.Yes)
                currentpage = myWindow.stackedWidget.currentIndex()
                myWindow.stackedWidget.setCurrentIndex(currentpage - 1)
                self.id_txt.setText("")
                self.nik_txt.setText("")
                self.pass_txt.setText("")
                self.pass2_txt.setText("")

            else:
                QMessageBox.information(self, '오류', "비밀번호가 일치하지 않습니다.", QMessageBox.Yes)
        conn.commit()
        conn.close()

    def btn_my(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage + 2)

    def btn_back(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage - 1)
        self.txt_total.clear()

    def btn_back2(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage - 2)
        self.login_pass_txt2.setText("")


    def btn_back3(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage - 3)

    def btn_back4(self):
        currentpage = myWindow.stackedWidget.currentIndex()
        myWindow.stackedWidget.setCurrentIndex(currentpage - 1)

    def btn_next(self):
        conn = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                               db='starDB', charset='utf8')
        conn.row_factory=sqlite3.Row
        cur = conn.cursor()  # connection으로부터 cursor생성
        self.lg_id = self.login_id_txt.text()

        cur.execute("SELECT N_name FROM join_data WHERE ID = '{}'".format(self.lg_id))
        result = cur.fetchall()
        self.d = str(result[0]['N_name'])
        print(self.d)
        self.nik_txt2.setText(self.d)

        lg_pw = self.login_pass_txt.text()
        lg_pw2 = self.login_pass_txt2.text()
        self.login_pass_txt2.setText("")
        self.up_id.setText("")

        if lg_pw == lg_pw2:
            currentpage = myWindow.stackedWidget.currentIndex()
            myWindow.stackedWidget.setCurrentIndex(currentpage + 1)

        else:
            # print(lg_pw)
            # print(lg_pw2)
            QMessageBox.information(self, '오류', "비밀번호가 일치하지 않습니다.", QMessageBox.Yes)
            self.login_pass_txt2.setText("")

        cur.execute("SELECT ID FROM join_data WHERE ID = '{}'".format(self.lg_id))
        result = cur.fetchall()
        self.i = str(result[0]['ID'])
        print(self.i)
        self.up_id.setText(self.i)
        conn.commit()
        conn.close()

    # def btn_up(self):
    #     conn = sqlite3.connect("Star_Bucks.db", isolation_level=None)  # 오토커밋 db연동
    #     cur = conn.cursor()  # connection으로부터 cursor생성
    #     pr_id = self.up_id.text()
    #     pr_nik = self.nik_txt2.toPlainText()
    #     pr_pass = self.uppw1.text()
    #     pr_pass2 = self.uppw2.text()
    #     print(pr_id)
    #
    #
    #     if not self.nikcheck2:
    #         QMessageBox.information(self, '오류', "닉네임 중복확인을 주세요.", QMessageBox.Yes)
    #
    #         return
    #
    #     if len(pr_pass) < 4 and len(pr_pass2) < 4:
    #         QMessageBox.information(self, '오류', "비밀번호를 4글자 이상 입력해주세요.", QMessageBox.Yes)
    #         self.uppw1.setText("")
    #         self.uppw2.setText("")
    #
    #         return
    #
    #     else:
    #         if pr_pass == pr_pass2:
    #             cur.execute("UPDATE join_data SET PASS = '{}' WHERE ID = '{}'".format(pr_pass, pr_id))
    #             cur.execute("UPDATE join_data SET N_name = '{}' WHERE ID = '{}'".format(pr_nik, pr_id))
    #
    #             result = cur.fetchall()
    #             print(result)
    #             QMessageBox.information(self, '성공', "회원정보 수정이 완료되었습니다.", QMessageBox.Yes)
    #             self.uppw1.setText("")
    #             self.uppw2.setText("")
    #             print("확인")
    #
    #         else:
    #             QMessageBox.information(self, '오류', "비밀번호가 일치하지 않습니다.", QMessageBox.Yes)
    #             print("취소")

    def can(self):
        self.americano1 = 0
        self.latte1 = 0
        self.caramel1 = 0
        self.moca1 = 0
        self.hazel1 = 0
        self.cappu1 = 0
        self.total1 = 0
        # self.add_ice1 =0
        self.menu_list1.clear()
        self.menu_list2.clear()
        self.txt_total.clear()
        self.money.clear()
        

    # def addice(self):
    #     self.addItemText = self.add_ice.text()
    #     self.menu_list1.addItem(self.addItemText)
        self.menulist = []
        self.menuprice = []

        if self.americano1 > 0:
            for i in range(self.americano1):
                self.menulist.append("아메리카노")
                self.menuprice.append("2000")
        if self.caramel1 > 0:
            for i in range(self.caramel1):
                self.menulist.append("카라멜 마끼아또")
                self.menuprice.append("2700")
        if self.latte1 > 0:
            for i in range(self.latte1):
                self.menulist.append("까페라떼")
                self.menuprice.append("2500")
        if self.moca1 > 0:
            for i in range(self.moca1):
                self.menulist.append("까페모카")
                self.menuprice.append("2700")
        if self.hazel1 > 0:
            for i in range(self.hazel1):
                self.menulist.append("헤이즐넛")
                self.menuprice.append("2600")
        if self.cappu1 > 0:
            for i in range(self.cappu1):
                self.menulist.append("까푸치노")
                self.menuprice.append("2900")
        print(self.menulist)

    def btn_text1(self):
        self.addItemText = self.label.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_text2(self):
        self.addItemText = self.label_2.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_text3(self):
        self.addItemText = self.label_3.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_text4(self):
        self.addItemText = self.label_4.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_text5(self):
        self.addItemText = self.label_5.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_text6(self):
        self.addItemText = self.label_6.text()
        self.menu_list1.addItem(self.addItemText)


    def btn_clicked_1(self, n):
        for i in range(n + 1):
            self.americano1 += 1

    def btn_clicked_2(self, n):
        for i in range(n + 1):
            self.latte1 += 1

    def btn_clicked_3(self, n):
        for i in range(n + 1):
            self.caramel1 += 1

    def btn_clicked_4(self, n):
        for i in range(n + 1):
            self.moca1 += 1

    def btn_clicked_5(self, n):
        for i in range(n + 1):
            self.hazel1 += 1

    def btn_clicked_6(self, n):
        for i in range(n + 1):
            self.cappu1 += 1

    def btn_clicked_ice(self, n):
        for i in range(n + 1):
            self.add_ice1 += 1

    def btn_clicked_add(self):
        self.menu_list2.clear()
        if self.americano1 > 0:
            self.menu_list2.append("아메리카노 {}잔".format(self.americano1))
        if self.latte1 > 0:
            self.menu_list2.append("라떼 {}잔".format(self.latte1))
        if self.caramel1 > 0:
            self.menu_list2.append("카라멜 마끼아또 {}잔".format(self.caramel1))
        if self.moca1 > 0:
            self.menu_list2.append("카페모카 {}잔".format(self.moca1))
        if self.hazel1 > 0:
            self.menu_list2.append("헤이즐넛 {}잔".format(self.hazel1))
        if self.cappu1 > 0:
            self.menu_list2.append("카푸치노 {}잔".format(self.cappu1))
        # if self.add_ice1 > 0:
        #     self.menu_list2.append("아이스 추가+{}".format(self.add_ice1))
        self.total1 = self.americano1 * 2000 + self.latte1 * 2500 + self.caramel1 * 2700 + self.moca1 * 2700 + self.hazel1 * 2600 + self.cappu1 * 2900 + self.add_ice1 * 300

    # def total(self):
    #     self.txt_total.append("총 가격은 {}원 입니다".format(self.total1))

    # def pm(self):
    #     self.menu_list4.clear()
    #     if self.americano1 > 0:
    #         self.menu_list2.append("아메리카노 {}잔".format(self.americano1))
    #     if self.latte1 > 0:
    #         self.menu_list2.append("라떼 {}잔".format(self.latte1))
    #     if self.caramel1 > 0:
    #         self.menu_list2.append("카라멜 마끼아또 {}잔".format(self.caramel1))
    #     if self.moca1 > 0:
    #         self.menu_list2.append("카페모카 {}잔".format(self.moca1))
    #     if self.hazel1 > 0:
    #         self.menu_list2.append("헤이즐넛 {}잔".format(self.hazel1))
    #     if self.cappu1 > 0:
    #         self.menu_list2.append("카푸치노 {}잔".format(self.cappu1))
    #     if self.add_ice1 > 0:
    #         self.menu_list2.append("아이스 추가+{}".format(self.add_ice1))
    #     self.txt_total.append("총 가격은 {}원 입니다".format(self.total1))

    def cash(self):
        paydate = time.strftime('%Y-%m-%d')
        paytime = time.strftime('%H:%M')
        # try:
        if int(self.money.toPlainText()) - int(self.total1) >= 0:
            self.menulist = []
            self.menuprice = []

            if self.americano1 > 0:
                for i in range(self.americano1):
                    self.menulist.append("아메리카노")
                    self.menuprice.append("2000")
            if self.caramel1 > 0:
                for i in range(self.caramel1):
                    self.menulist.append("카라멜 마끼아또")
                    self.menuprice.append("2700")
            if self.latte1 > 0:
                for i in range(self.latte1):
                    self.menulist.append("까페라떼")
                    self.menuprice.append("2500")
            if self.moca1 > 0:
                for i in range(self.moca1):
                    self.menulist.append("까페모카")
                    self.menuprice.append("2700")
            if self.hazel1 > 0:
                for i in range(self.hazel1):
                    self.menulist.append("헤이즐넛")
                    self.menuprice.append("2600")
            if self.cappu1 > 0:
                for i in range(self.cappu1):
                    self.menulist.append("까푸치노")
                    self.menuprice.append("2900")

            for i in self.menulist:
                if i == "아메리카노":
                    p = 2000
                    print(i)
                    print(p)
                elif i == "카라멜 마끼아또":
                    p = 2700
                elif i == "까페라떼":
                    p = 2500
                elif i == "까페모카":
                    p = 2700
                elif i == "까푸치노":
                    p = 2900
                elif i == "헤이즐넛":
                    p = 2600

                conn1 = pymysql.connect(host='10.10.21.111', port=3306, user='London_jini', password='starDB1234@',
                                        db='starDB', charset='utf8')
                cur1 = conn1.cursor()

                conn2 = pymysql.connect(host='10.10.21.118', port=3306, user='London', password='starDB1234@',
                                        db='starDB', charset='utf8')
                cur2 = conn2.cursor() # connection으로부터 cursor생성

                cur1.execute("INSERT INTO Order_data_London VALUES('{}','{}','{}','{}','{}','{}')".format(self.lg_id,i,p,paydate,paytime,"런던본점"))
                cur1.fetchall()
                cur2.execute("INSERT INTO Order_data VALUES('{}','{}','{}','{}','{}','{}')".format(self.lg_id, i, p, paydate, paytime, "런던본점"))
                cur2.fetchall()
                print(self.menuprice)
                self.msg.setIcon(QMessageBox.Question)
                self.msg.setWindowTitle('결제확인')
                self.msg.setText("결제가 완료되었습니다.\n 잔돈은 {}입니다.".format(int(self.money.toPlainText()) - int(self.total1)))
                self.msg.setStandardButtons(QMessageBox.Ok)
                self.msg.exec_()
                conn1.commit()
                conn1.close()

                conn2.commit()
                conn2.close()

        else:
            self.msg.setIcon(QMessageBox.Information)
            self.msg.setWindowTitle('결제확인')
            self.msg.setText("금액이 {}원 부족합니다.".format(int(self.total1)-int(self.money.toPlainText())))
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
        # except:
        #     self.msg.setIcon(QMessageBox.Information)
        #     self.msg.setWindowTitle('결제확인')
        #     self.msg.setText("세상에 문자나 음수나 특수문자돈이 어디있습니까 휴먼?")
        #     self.msg.setStandardButtons(QMessageBox.Ok)
        #     self.msg.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()



