import sys, re, sqlite3
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from datetime import *
########################################################################################################################
########################################################################################################################
UI = '../_qt_ui/newsb.ui'
########################################################################################################################
########################################################################################################################
class Simplify:
    def images(self):
        # 홈 로고
        self.label_start_logo.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        self.label_start_logo_2.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        self.label_start_logo_3.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        self.label_start_logo_4.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        self.label_start_logo_5.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        self.label_end_logo.setStyleSheet('image:url(../_qt_ui/icon/icon_sb640.png);')
        # 장바구니
        self.label_purchase_image.setStyleSheet('image:url(../_qt_ui/icon/icon_insert64.png);')
        self.label_purchase_image2.setStyleSheet('image:url(../_qt_ui/icon/icon_receive64.png);')
        # 탈퇴
        self.label_close_end_logo.setStyleSheet('image:url(../_qt_ui/icon/icon_check96.png);')
        # 커피 이미지
        self.label_image_1_1.setStyleSheet('image:url(../_qt_ui/menu/1_1.jpg);')
        self.label_image_1_2.setStyleSheet('image:url(../_qt_ui/menu/1_2.jpg);')
        self.label_image_1_3.setStyleSheet('image:url(../_qt_ui/menu/1_3.jpg);')
        self.label_image_1_4.setStyleSheet('image:url(../_qt_ui/menu/1_4.jpg);')
        self.label_image_1_5.setStyleSheet('image:url(../_qt_ui/menu/1_5.jpg);')
        self.label_image_1_6.setStyleSheet('image:url(../_qt_ui/menu/1_6.jpg);')
        self.label_image_1_7.setStyleSheet('image:url(../_qt_ui/menu/1_7.jpg);')
        self.label_image_1_8.setStyleSheet('image:url(../_qt_ui/menu/1_8.jpg);')
        self.label_image_1_9.setStyleSheet('image:url(../_qt_ui/menu/1_9.jpg);')
        self.label_image_1_90.setStyleSheet('image:url(../_qt_ui/menu/1_10.jpg);')
        self.label_image_1_91.setStyleSheet('image:url(../_qt_ui/menu/1_11.jpg);')
        self.label_image_3_1.setStyleSheet('image:url(../_qt_ui/menu/3_1.jpg);')
        self.label_image_3_2.setStyleSheet('image:url(../_qt_ui/menu/3_2.jpg);')
        self.label_image_3_3.setStyleSheet('image:url(../_qt_ui/menu/3_3.jpg);')
        self.label_image_3_4.setStyleSheet('image:url(../_qt_ui/menu/3_4.jpg);')
        self.label_image_3_5.setStyleSheet('image:url(../_qt_ui/menu/3_5.jpg);')
        self.label_image_3_6.setStyleSheet('image:url(../_qt_ui/menu/3_6.jpg);')
        self.label_image_3_7.setStyleSheet('image:url(../_qt_ui/menu/3_7.jpg);')
        self.label_image_3_8.setStyleSheet('image:url(../_qt_ui/menu/3_8.jpg);')
        self.label_image_3_9.setStyleSheet('image:url(../_qt_ui/menu/3_9.jpg);')
        self.label_image_3_90.setStyleSheet('image:url(../_qt_ui/menu/3_10.jpg);')
        self.label_image_3_91.setStyleSheet('image:url(../_qt_ui/menu/3_11.jpg);')
########################################################################################################################
########################################################################################################################
class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, QStyleOptionViewItem, QModelIndex):
        QStyledItemDelegate.initStyleOption(self, QStyleOptionViewItem, QModelIndex)
        QStyleOptionViewItem.displayAlignment = Qt.AlignCenter
########################################################################################################################
########################################################################################################################
class greater:
    # 총 구매 금액
    money = 0

    # 회원번호이자 회원고유번호를 만들기 위해(해놓고 의미 없어짐)
    __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
    __c = __connect.cursor()
    qy = "SELECT MAX(MNO) FROM SMINFO"
    __c.execute(qy)
    iy = __c.fetchone()
    count = 0
    print(type(iy[0]), "1")
    if iy[0] == None:
        count = 1
    else:
        count = iy[0] + 1

    # 로그인시 회원정보를 담는 리스트
    account_info = []

    # 결제시 db연동 위한 리스트
    menu_list = []
    price_list = []
    quantity_list = []
    agg_list = []

    # 주문번호 생성
    # time = datetime.now()
    # odnotime = time.strftime('%Y%M%S')
########################################################################################################################
########################################################################################################################
class window(QDialog, Simplify):
    def __init__(self):
        QDialog.__init__(self, None, Qt.WindowStaysOnTopHint)
        Simplify.__init__(self)
        uic.loadUi(UI, self)
        Simplify.images(self)
        self.offset = None
        self.setWindowFlag(Qt.FramelessWindowHint)
        # 페이지 고정
        self.stackedWidget.setCurrentWidget(self.page_start)
        ################################################################################################################
        # 스타일시트
        self.stylePopupOk = ("""
        QLineEdit{font: 75 12pt "맑은 고딕"; border-radius: 5px; border:2px solid rgb(0, 112, 74); padding-left: 20px; padding-right: 20px;}
        QLineEdit:focus{border: 2px solid rgb(65, 205, 82)}
        """)
        self.stylePopupError = ("""
        QLineEdit{font: 75 12pt "맑은 고딕"; border-radius: 5px; border:2px solid rgb(255, 0, 0); padding-left: 20px; padding-right: 20px;}
        """)
        styleCheck = ("""
                        QCheckBox{font: 11pt "맑은 고딕"; color: rgb(0, 102, 51);}
                        QCheckBox::indicator{border: 2px solid rgb(193, 193, 193); width: 28px; height: 28px; border-radius: 16px;\
                        background-color: rgb(193, 193, 193); image:url(../_qt_ui/icon/icon_check24.png);}
                        QCheckBox::indicator:checked{border: 2px solid rgb(0, 102, 51); background-color: rgb(0, 102, 51);}
                        """)
        # 체크박스
        self.checkBox.setStyleSheet(styleCheck)
        self.checkBox_clause_1.setStyleSheet(styleCheck)
        self.checkBox_clause_2.setStyleSheet(styleCheck)
        self.checkBox_clause_3.setStyleSheet(styleCheck)
        self.checkBox_account_close.setStyleSheet(styleCheck)
        ################################################################################################################
        # 메뉴 추가
        self.pushButton_1_1.clicked.connect(
            lambda state, menu='아이스크림 블렌딩 콜드 브루', price=1000, spin=self.spinBox_1_1: self.add(state, menu, price, spin))
        self.pushButton_1_2.clicked.connect(
            lambda state, menu='나이트로 바닐라 크림', price=1000, spin=self.spinBox_1_2: self.add(state, menu, price, spin))
        self.pushButton_1_3.clicked.connect(
            lambda state, menu='나이트로 콜드 브루', price=1000, spin=self.spinBox_1_3: self.add(state, menu, price, spin))
        self.pushButton_1_4.clicked.connect(
            lambda state, menu='돌체 콜드 브루', price=1500, spin=self.spinBox_1_4: self.add(state, menu, price, spin))
        self.pushButton_1_5.clicked.connect(
            lambda state, menu='바닐라 크림 콜드 브루', price=1500, spin=self.spinBox_1_5: self.add(state, menu, price, spin))
        self.pushButton_1_6.clicked.connect(
            lambda state, menu='벨벳 다크 모카 나이트로', price=1500, spin=self.spinBox_1_6: self.add(state, menu, price, spin))
        self.pushButton_1_7.clicked.connect(
            lambda state, menu='제주 비자림 콜드 브루', price=2000, spin=self.spinBox_1_7: self.add(state, menu, price, spin))
        self.pushButton_1_8.clicked.connect(
            lambda state, menu='콜드 브루', price=2000, spin=self.spinBox_1_8: self.add(state, menu, price, spin))
        self.pushButton_1_9.clicked.connect(
            lambda state, menu='콜드 브루 몰트', price=2000, spin=self.spinBox_1_9: self.add(state, menu, price, spin))
        self.pushButton_1_90.clicked.connect(
            lambda state, menu='콜드 브루 오트 라떼', price=2500, spin=self.spinBox_1_90: self.add(state, menu, price, spin))
        self.pushButton_1_91.clicked.connect(
            lambda state, menu='콜드 브루 플로트', price=2500, spin=self.spinBox_1_91: self.add(state, menu, price, spin))
        self.pushButton_3_1.clicked.connect(
            lambda state, menu='에스프레소 콘 파나', price=1000, spin=self.spinBox_3_1: self.add(state, menu, price, spin))
        self.pushButton_3_2.clicked.connect(
            lambda state, menu='에스프레소 마키아또', price=1000, spin=self.spinBox_3_2: self.add(state, menu, price, spin))
        self.pushButton_3_3.clicked.connect(
            lambda state, menu='아이스 카페 아메리카노', price=1000, spin=self.spinBox_3_3: self.add(state, menu, price, spin))
        self.pushButton_3_4.clicked.connect(
            lambda state, menu='카페 아메리카노', price=1500, spin=self.spinBox_3_4: self.add(state, menu, price, spin))
        self.pushButton_3_5.clicked.connect(
            lambda state, menu='아이스 카라멜 마키아또', price=1500, spin=self.spinBox_3_5: self.add(state, menu, price, spin))
        self.pushButton_3_6.clicked.connect(
            lambda state, menu='카라멜 마키아또', price=1500, spin=self.spinBox_3_6: self.add(state, menu, price, spin))
        self.pushButton_3_7.clicked.connect(
            lambda state, menu='아이스 카푸치노', price=2000, spin=self.spinBox_3_7: self.add(state, menu, price, spin))
        self.pushButton_3_8.clicked.connect(
            lambda state, menu='카푸치노', price=2000, spin=self.spinBox_3_8: self.add(state, menu, price, spin))
        self.pushButton_3_9.clicked.connect(
            lambda state, menu='라벤더 카페 브레베', price=2000, spin=self.spinBox_3_9: self.add(state, menu, price, spin))
        self.pushButton_3_90.clicked.connect(
            lambda state, menu='럼 샷 코르타도', price=2500, spin=self.spinBox_3_90: self.add(state, menu, price, spin))
        self.pushButton_3_91.clicked.connect(
            lambda state, menu='바닐라 빈 라떼', price=2500, spin=self.spinBox_3_91: self.add(state, menu, price, spin))
        ################################################################################################################
        # 장바구니 목록
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.tableWidget.setColumnWidth(1, 70)
        # self.tableWidget.setColumnWidth(2, 50)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.tableWidget.setColumnWidth(3, 80)
        self.tableWidget.setItemDelegateForColumn(0, AlignDelegate(self.tableWidget))
        self.tableWidget.setItemDelegateForColumn(1, AlignDelegate(self.tableWidget))
        self.tableWidget.setItemDelegateForColumn(2, AlignDelegate(self.tableWidget))
        self.tableWidget.setItemDelegateForColumn(3, AlignDelegate(self.tableWidget))
        ################################################################################################################
        # 탑 로그인
        self.pushButton_login.clicked.connect(self.login_top)

        # 시작 페이지에서
        self.pushButton_home.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_home))
        self.pushButton_start_login.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_login))
        self.pushButton_start_signup.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_clause))

        # 메뉴 버튼들
        self.pushButton1.clicked.connect(lambda state, button = self.pushButton1 : self.select_menu(state, button))
        self.pushButton2.clicked.connect(lambda state, button = self.pushButton2 : self.select_menu(state, button))
        self.pushButton3.clicked.connect(lambda state, button = self.pushButton3 : self.select_menu(state, button))
        self.pushButton4.clicked.connect(lambda state, button = self.pushButton4 : self.select_menu(state, button))
        self.pushButton5.clicked.connect(lambda state, button = self.pushButton5 : self.select_menu(state, button))
        self.pushButton_order.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_order))
        self.pushButton_close.clicked.connect(self.windowclose)

        # 로그인 페이지에서
        self.lineEdit_id.textEdited.connect(lambda state, select = self.lineEdit_id : self.login_indicator(state, select))
        self.lineEdit_pw.textEdited.connect(lambda state, select = self.lineEdit_pw : self.login_indicator(state, select))
        self.pushButton_login_login.clicked.connect(self.login_login)
        self.pushButton_login_signup.clicked.connect(self.login_signup)

        # 약관동의 페이지에서
        self.checkBox_clause_1.clicked.connect(lambda state, clicked = self.checkBox_clause_1 : self.clause_checkbox(state, clicked))
        self.checkBox_clause_2.clicked.connect(lambda state, clicked = self.checkBox_clause_2 : self.clause_checkbox(state, clicked))
        self.pushButton_clause.clicked.connect(self.clause_next)

        # 회원가입 페이지에서
        self.lineEdit_signup_id.textEdited.connect(lambda state, select=self.lineEdit_signup_id: self.signup_indicator(state, select))
        self.lineEdit_signup_pw.textEdited.connect(lambda state, select=self.lineEdit_signup_pw: self.signup_indicator(state, select))
        self.lineEdit_signup_pw2.textEdited.connect(lambda state, select=self.lineEdit_signup_pw2: self.signup_indicator(state, select))
        self.lineEdit_signup_name.textEdited.connect(lambda state, select=self.lineEdit_signup_name: self.signup_indicator(state, select))
        self.lineEdit_signup_phone.textEdited.connect(lambda state, select=self.lineEdit_signup_phone: self.signup_indicator(state, select))
        self.lineEdit_signup_mail.textEdited.connect(lambda state, select=self.lineEdit_signup_mail: self.signup_indicator(state, select))
        self.lineEdit_signup_nick.textEdited.connect(lambda state, select=self.lineEdit_signup_nick: self.signup_indicator(state, select))
        self.pushButton_signup.clicked.connect(self.signup)

        # 장바구니에서
        self.pushButton_order_del.clicked.connect(self.cancel_item)
        self.pushButton_order_pay.clicked.connect(self.pay)

        # 결제 부분
        self.label_total_money.setText("{}원".format(greater.money))

        ################################################################################################################
        # 마이페이지 구간
        ################################################################################################################
        self.pushButton_my.setEnabled(False)
        self.pushButton_logout.setEnabled(False)

        # 탑에서 회원정보
        self.pushButton_my.clicked.connect(lambda state, button = self.pushButton_my : self.clear_list(state, button))
        self.pushButton_purchase_list.clicked.connect(lambda state, button = self.pushButton_purchase_list : self.clear_list(state, button))

        # 회원정보 수정
        self.pushButton_account_update.clicked.connect(self.account_update)
        # 회원정보 수정 비밀번호 재확인
        self.lineEdit_check.textEdited.connect(lambda state, edit = self.lineEdit_check : self.check_indicator(state, edit))
        # self.pushButton_purchase_list.clicked.connect(lambda : self.stackedWidget_my.setCurrentWidget(self.page_check))
        self.pushButton_check.clicked.connect(self.check)

        self.pushButton_account_update_pw.clicked.connect(lambda state, button = self.pushButton_account_update_pw : self.update_account(state, button))
        self.pushButton_account_update_info.clicked.connect(lambda state, button = self.pushButton_account_update : self.update_account(state, button))

        self.lineEdit_account_pw.textEdited.connect(lambda state, select=self.lineEdit_account_pw: self.account_indicator(state, select))
        self.lineEdit_account_pw2.textEdited.connect(lambda state, select=self.lineEdit_account_pw2: self.account_indicator(state, select))
        self.lineEdit_account_phone.textEdited.connect(lambda state, select=self.lineEdit_account_phone: self.account_indicator(state, select))
        self.lineEdit_account_mail.textEdited.connect(lambda state, select=self.lineEdit_account_mail: self.account_indicator(state, select))
        self.lineEdit_account_nick.textEdited.connect(lambda state, select=self.lineEdit_account_nick: self.account_indicator(state, select))

        self.checkBox_pw.clicked.connect(lambda state, clicked = self.checkBox_pw : self.account_checkbox(state, clicked))
        self.checkBox_pw2.clicked.connect(lambda state, clicked = self.checkBox_pw2 : self.account_checkbox(state, clicked))

        # 주문내역 조회
        self.pushButton_list_iy.clicked.connect(self.purchase_list)
        # self.comboBox_list_1.setAlignment(Qt.AlignRight)

        # 회원탈퇴
        self.pushButton_account_close.clicked.connect(self.account_close)
        self.pushButton_account_close_check.clicked.connect(self.close_account)
        self.checkBox_account_close.clicked.connect(self.close_checkbox)
        # 회원탈퇴 비밀번호 재확인
        self.lineEdit_check2.textEdited.connect(lambda state, edit = self.lineEdit_check2 : self.check_indicator(state, edit))
        self.pushButton_check2.clicked.connect(self.check2)

        # logout
        self.pushButton_logout.clicked.connect(self.logout)

########################################################################################################################
    # 슬롯
########################################################################################################################
    # 메뉴누를 때
    def select_menu(self, state, button):
        self.label_change.clear()
        self.label_order_info.clear()
        if button == self.pushButton1:
            self.scrollArea_1.verticalScrollBar().setValue(0)
            self.stackedWidget.setCurrentWidget(self.page_1)
        elif button == self.pushButton2:
            self.stackedWidget.setCurrentWidget(self.page_2)
        elif button == self.pushButton3:
            self.scrollArea_3.verticalScrollBar().setValue(0)
            self.stackedWidget.setCurrentWidget(self.page_3)
        elif button == self.pushButton4:
            self.stackedWidget.setCurrentWidget(self.page_4)
        else:
            self.stackedWidget.setCurrentWidget(self.page_5)

    # 로그인 탑버튼
    def login_top(self):
        self.lineEdit_id.setStyleSheet(self.stylePopupOk)
        if self.checkBox.isChecked() == True:
            pass
        else:
            self.lineEdit_id.clear()
        self.lineEdit_pw.setStyleSheet(self.stylePopupOk)
        self.lineEdit_pw.clear()
        self.label_login_info0.clear()
        self.stackedWidget.setCurrentWidget(self.page_login)
    ####################################################################################################################
    ####################################################################################################################
    # 로그인 페이지에서
    def login_indicator(self, state, select):
        if select == self.lineEdit_id:
            if self.lineEdit_id.text() != "" or self.lineEdit_pw.text() != "":
                self.lineEdit_id.setStyleSheet(self.stylePopupOk)
                self.lineEdit_pw.setStyleSheet(self.stylePopupOk)
                self.label_login_info0.clear()
        else:
            if self.lineEdit_pw.text() != "" or self.lineEdit_id.text() != "":
                self.lineEdit_pw.setStyleSheet(self.stylePopupOk)
                self.lineEdit_id.setStyleSheet(self.stylePopupOk)
                self.label_login_info0.clear()

    # 로그인할 때
    def login_login(self):
        __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        __c = __connect.cursor()
        qy = "SELECT ID, PW, NAME, BIRTH, PHONE, EMAIL, NICK FROM SMINFO WHERE ID='{}'"
        check_id = self.lineEdit_id.text()
        __c.execute(qy.format(check_id))
        iy = __c.fetchall()
        if not iy:
            if self.lineEdit_id.text() == "":
                self.label_login_info0.setText("계정을 입력해 주세요.")
                self.lineEdit_id.setStyleSheet(self.stylePopupError)
            else:
                if self.lineEdit_pw.text() == "":
                    self.label_login_info0.setText("비밀번호를 입력해 주세요.")
                    self.lineEdit_pw.setStyleSheet(self.stylePopupError)
                else:
                    self.label_login_info0.setText("계정 혹은 비밀번호가 일치하지 않습니다. 다시 확인해 주세요.")
                    self.lineEdit_id.setStyleSheet(self.stylePopupError)
                    self.lineEdit_pw.setStyleSheet(self.stylePopupError)
        else:  # iy != []:
            id, pw, name, birth, phone, email, nick = zip(*iy)
            my_info = [id, pw, name, birth, phone, email, nick]
            for value in my_info:
                greater.account_info.append(value[0])
            print(greater.account_info)
            time = datetime.now()
            now = time.strftime('%Y-%m-%d/%H:%M:%S')
            if pw[0] == self.lineEdit_pw.text():
                if self.checkBox.isChecked() == True:
                    self.pushButton_my.setEnabled(True)
                    self.pushButton_my.setText('회원정보')
                    self.pushButton_logout.setEnabled(True)
                    self.pushButton_logout.setText('로그아웃')
                    self.label_top.setText("반갑습니다 {} 님".format(name[0]))
                    self.pushButton_login.setEnabled(False)
                    self.pushButton_login.setText("")
                    ##########################################################
                    self.lineEdit_id.setText(greater.account_info[0])  # 체크박스
                    self.lineEdit_pw.clear()
                    # self.lineEdit_id.setStyleSheet(self.stylePopupOk)
                    # self.lineEdit_pw.setStyleSheet(self.stylePopupOk)
                    # self.label_login_info0.clear()
                    self.stackedWidget.setCurrentWidget(self.page_home)
                    qy = "UPDATE SMINFO SET RCD = '{}' WHERE ID = '{}'"
                    __c.execute(qy.format(now, id[0]))
                else:
                    self.pushButton_my.setEnabled(True)
                    self.pushButton_my.setText('회원정보')
                    self.pushButton_logout.setEnabled(True)
                    self.pushButton_logout.setText('로그아웃')
                    self.label_top.setText("반갑습니다 {} 님".format(name[0]))
                    self.pushButton_login.setEnabled(False)
                    self.pushButton_login.setText("")
                    #################################
                    self.lineEdit_id.clear()  # 체크박스
                    self.lineEdit_pw.clear()
                    # self.lineEdit_id.setStyleSheet(self.stylePopupOk)
                    # self.lineEdit_pw.setStyleSheet(self.stylePopupOk)
                    # self.label_login_info0.clear()
                    self.stackedWidget.setCurrentWidget(self.page_home)
                    qy = "UPDATE SMINFO SET RCD = '{}' WHERE ID = '{}'"
                    __c.execute(qy.format(now, id[0]))
            else:
                if self.lineEdit_pw.text() == "":
                    self.label_login_info0.setText("비밀번호를 입력해 주세요.")
                    greater.account_info.clear()
                else:
                    self.label_login_info0.setText("계정 혹은 비밀번호가 일치하지 않습니다. 다시 확인해 주세요.")
                    self.lineEdit_id.setStyleSheet(self.stylePopupError)
                    self.lineEdit_pw.setStyleSheet(self.stylePopupError)
                    greater.account_info.clear()

    def login_signup(self):
        self.checkBox_clause_1.setChecked(False)
        self.checkBox_clause_2.setChecked(False)
        self.checkBox_clause_3.setChecked(False)
        self.label_clause_info.clear()
        # focus
        self.scrollArea_clause.verticalScrollBar().setValue(0)
        self.stackedWidget.setCurrentWidget(self.page_clause)
    ####################################################################################################################
    ####################################################################################################################
    # 약관동의 페이지에서
    def clause_checkbox(self, state, clicked):
        if clicked == self.checkBox_clause_1:
            if self.checkBox_clause_1.isChecked() == True and\
                    self.checkBox_clause_2.isChecked() == True:
                self.label_clause_info.clear()
        else:
            if self.checkBox_clause_1.isChecked() == True and \
                    self.checkBox_clause_2.isChecked() == True:
                self.label_clause_info.clear()

    def clause_next(self):
        if self.checkBox_clause_1.isChecked() == True and self.checkBox_clause_2.isChecked() == True:
            self.stackedWidget.setCurrentWidget(self.page_signup)
            self.lineEdit_signup_id.clear()
            self.lineEdit_signup_pw.clear()
            self.lineEdit_signup_pw2.clear()
            self.lineEdit_signup_name.clear()
            self.lineEdit_signup_phone.clear()
            self.lineEdit_signup_mail.clear()
            self.lineEdit_signup_nick.clear()
            self.label_signup_info.clear()
            self.label_signup_info_1.clear()
            self.label_signup_info_2.clear()
            self.label_signup_info_3.clear()
            self.label_signup_info_4.clear()
            self.label_signup_info_5.clear()
            self.label_signup_info_6.clear()
            self.label_signup_info_7.clear()
            self.lineEdit_signup_id.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_pw.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_name.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_mail.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_phone.setStyleSheet(self.stylePopupOk)
            self.lineEdit_signup_nick.setStyleSheet(self.stylePopupOk)
            # focus
            self.lineEdit_signup_id.setFocus()
            self.scrollArea_signup.verticalScrollBar().setValue(0)
        else:
            self.label_clause_info.setText('필수 이용약관에 동의 하셔야 합니다.')
    ####################################################################################################################
    ####################################################################################################################
    # 회원가입 페이지에서
    def signup_indicator(self, state, select):
        self.label_signup_info.clear()
        __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        __c = __connect.cursor()
        qy = "SELECT ID FROM SMINFO"
        __c.execute(qy)
        iy = __c.fetchall()
        check_all_id = list(map(lambda val: val[0], iy))
        # 아이디
        if select == self.lineEdit_signup_id:
            if len(self.lineEdit_signup_id.text()) < 4 or\
                    self.lineEdit_signup_id.text().isalnum() == False:
                self.label_signup_info_1.setText('영문(대소문자 구분 없음), 숫자로 4~13자리만 입력해 주세요.')
                self.lineEdit_signup_id.setStyleSheet(self.stylePopupError)
            elif self.lineEdit_signup_id.text() in check_all_id:
                self.label_signup_info_1.setText('이미 사용 중인 아이디 입니다.')
                self.lineEdit_signup_id.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_1.clear()
                self.lineEdit_signup_id.setStyleSheet(self.stylePopupOk)
        # 비번
        elif select == self.lineEdit_signup_pw:
            if len(self.lineEdit_signup_pw.text()) < 10 or \
                    self.lineEdit_signup_pw.text().isdigit() == True or\
                    self.lineEdit_signup_pw.text().isalpha() == True or\
                    self.lineEdit_signup_pw.text().isalnum() == False:
                self.label_signup_info_2.setText('영문, 숫자 혼합하여 10~20자 이내로 입력해 주세요.')
                self.lineEdit_signup_pw.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_2.clear()
                self.lineEdit_signup_pw.setStyleSheet(self.stylePopupOk)
                if self.lineEdit_signup_pw2.text() != "" and self.lineEdit_signup_pw.text() != self.lineEdit_signup_pw2.text():
                    self.label_signup_info_3.setText('비밀번호가 일치하지 않습니다.')
                    self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupError)
                else:# self.lineEdit_signup_pw.text() == self.lineEdit_signup_pw2.text():
                    self.label_signup_info_3.clear()
                    self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupOk)
        # 비번2
        elif select == self.lineEdit_signup_pw2:
            if self.lineEdit_signup_pw.text() != self.lineEdit_signup_pw2.text():
                self.label_signup_info_3.setText('비밀번호가 일치하지 않습니다.')
                self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_3.clear()
                self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupOk)
        # 이름
        elif select == self.lineEdit_signup_name:
            hangeul = re.sub('[^가-힣]', "", self.lineEdit_signup_name.text())
            if len(hangeul) < 2:
                self.label_signup_info_4.setText('이름이 아닙니다.')
                self.lineEdit_signup_name.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_4.clear()
                self.lineEdit_signup_name.setStyleSheet(self.stylePopupOk)
        # 번호
        elif select == self.lineEdit_signup_phone:
            if len(self.lineEdit_signup_phone.text()) < 11 or \
                    "010" not in self.lineEdit_signup_phone.text() or \
                    self.lineEdit_signup_phone.text().isdigit() == False:
                self.label_signup_info_5.setText('"-"를 제외하고 번호 11자리를 입력해 주세요.')
                self.lineEdit_signup_phone.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_5.clear()
                self.lineEdit_signup_phone.setStyleSheet(self.stylePopupOk)
        # 메일
        elif select == self.lineEdit_signup_mail:
            if ("@" and ".") not in self.lineEdit_signup_mail.text() or\
                    len(self.lineEdit_signup_mail.text()) < 8:
                self.label_signup_info_6.setText('이메일 형식이 아닙니다.')
                self.lineEdit_signup_mail.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_6.clear()
                self.lineEdit_signup_mail.setStyleSheet(self.stylePopupOk)
        # 닉네임
        elif select == self.lineEdit_signup_nick:
            hangeul = re.sub('[^가-힣]', "", self.lineEdit_signup_nick.text())
            print(len(hangeul))
            if len(hangeul) < 1 or len(hangeul) > 6:
                self.label_signup_info_7.setText('한글 6자리 이내로 입력해 주세요.')
                self.lineEdit_signup_nick.setStyleSheet(self.stylePopupError)
            else:
                self.label_signup_info_7.clear()
                self.lineEdit_signup_nick.setStyleSheet(self.stylePopupOk)
        else:
            pass

    # 회원가입할 때
    def signup(self):
        if self.lineEdit_signup_id.text() == "":
            self.label_signup_info.setText('아이디를 입력해 주세요')
            self.lineEdit_signup_id.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_pw.text() == "":
            self.label_signup_info.setText('비밀번호를 입력해주세요')
            self.lineEdit_signup_pw.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_pw2.text() == "":
            self.label_signup_info.setText('비밀번호를 입력해주세요')
            self.lineEdit_signup_pw2.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_name.text() == "":
            self.label_signup_info.setText('이름을 입력해주세요')
            self.lineEdit_signup_name.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_phone.text() == "":
            self.label_signup_info.setText('번호를 입력해주세요')
            self.lineEdit_signup_phone.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_mail.text() == "":
            self.label_signup_info.setText('메일을 입력해주세요')
            self.lineEdit_signup_mail.setStyleSheet(self.stylePopupError)
        elif self.lineEdit_signup_nick.text() == "":
            self.label_signup_info.setText('닉네임을 입력해주세요')
            self.lineEdit_signup_nick.setStyleSheet(self.stylePopupError)
        else:
            __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            __c = __connect.cursor()
            time = datetime.now()
            sin = time.strftime('%y%M%S')
            now = time.strftime('%Y-%m-%d/%H:%M:%S')
            if self.label_signup_info_1.text() == "" and self.label_signup_info_2.text() == "" and \
                    self.label_signup_info_3.text() == "" and self.label_signup_info_4.text() == "" and \
                    self.label_signup_info_5.text() == "" and self.label_signup_info_6.text() == "" and \
                    self.label_signup_info_7.text() == "" and self.label_signup_info.text() == "":
                ########################################################################################################
                id = self.lineEdit_signup_id.text()
                extract_num = self.lineEdit_signup_phone.text()
                extract_num = extract_num[-2:]
                sin = (sin + extract_num)
                pw = self.lineEdit_signup_pw.text()
                name = self.lineEdit_signup_name.text()
                birth = ((self.comboBox_year.currentText()) + (self.comboBox_month.currentText()) + (
                    self.comboBox_day.currentText()))
                phone = self.lineEdit_signup_phone.text()
                email = self.lineEdit_signup_mail.text()
                nick = self.lineEdit_signup_nick.text()
                rcd = "-"
                rcp = "-"
                ########################################################################################################
                qy = "INSERT INTO SMINFO VALUES(?,?,?,?,?,?,?,?,?,?,?,?)"
                __c.execute(qy, (greater.count, now, id, sin, pw, name, birth, phone, email, nick, rcd, rcp))
                self.stackedWidget.setCurrentWidget(self.page_signup_end)
    ####################################################################################################################
    ####################################################################################################################
    # 메뉴 페이지에서 메뉴 추가할 때
    def add(self, state, menu, price, spin):
        if spin.value() == 0:
            pass
        else:
            row_number = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_number)
            self.tableWidget.setItem(row_number, 0, QTableWidgetItem(menu))
            greater.menu_list.append(menu)
            ################################################################
            self.tableWidget.setItem(row_number, 1, QTableWidgetItem("{}원".format(price)))
            greater.price_list.append(price)
            #####################################################################################
            self.tableWidget.setItem(row_number, 2, QTableWidgetItem("{}개".format(spin.value())))
            greater.quantity_list.append(spin.value())
            #############################################################################################
            self.tableWidget.setItem(row_number, 3, QTableWidgetItem("{}원".format(price * spin.value())))
            greater.agg_list.append(price * spin.value())
            #####################################
            greater.money += price * spin.value()
            self.label_total_money.setText("{}원".format(greater.money))
            spin.setValue(0)
    ####################################################################################################################
    ####################################################################################################################
    # 장바구니 페이지에서
    def cancel_item(self):
        if self.tableWidget.currentRow() == -1:
            pass
        else:
            returned = self.tableWidget.selectedItems()
            # 메뉴
            item0 = QTableWidgetItem(returned[0]).text()
            # 가격
            exclude_won1 = re.findall(r'\d+', QTableWidgetItem(returned[1]).text())
            item1 = exclude_won1[0]
            # 수량
            exclude_pcs = re.findall(r'\d+', QTableWidgetItem(returned[2]).text())
            item2 = exclude_pcs[0]
            # 가격x수량
            exclude_won2 = re.findall(r'\d+', QTableWidgetItem(returned[3]).text())
            item3 = exclude_won2[0]
            greater.menu_list.remove(item0)
            greater.price_list.remove(int(item1))
            greater.quantity_list.remove(int(item2))
            greater.agg_list.remove(int(item3))
            print(greater.menu_list)
            print(greater.quantity_list)
            print(greater.agg_list)
            row = self.tableWidget.currentRow()
            onlynumber = re.findall(r'\d+', self.tableWidget.item(row, 3).text())
            onlynumber = onlynumber[0]
            self.tableWidget.removeRow(row)
            greater.money -= int(onlynumber)
            self.label_total_money.setText("{}원".format(greater.money))

    # 결제할 때
    def pay(self):
        try:
            time = datetime.now()
            paydate = time.strftime('%Y/%m/%d')
            paytime = time.strftime('%H:%M:%S')
            __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            __c = __connect.cursor()
            number = re.findall(r'\d+', self.label_total_money.text())
            number = number[0]
            print(type(number))
            if int(self.lineEdit_inputmoney.text()) < int(number):
                self.label_order_info.setStyleSheet("""
                QLabel{font: 75 12pt "맑은 고딕"; color: rgb(255, 0, 0); background-color: rgb(255, 255, 255);}
                """)
                self.label_order_info.setText('금액이 부족합니다.')
            elif int(self.lineEdit_inputmoney.text()) >= int(number):
                if greater.account_info != []:
                    ####################################################################################################
                    qy1 = """
                    SELECT COUNT(*) FROM PAYINFO
                    WHERE ID = '{}' AND PAYDATE = STRFTIME('%Y/%m/%d', 'now', 'localtime')
                    """
                    __c.execute(qy1.format(greater.account_info[0]))
                    iy = __c.fetchone()
                    print(type(iy[0]), "2")
                    print(iy[0])
                    if iy[0] == 0:
                        count = 0
                    else:
                        count = iy[0]
                    print(count)
                    # 구매 내역
                    for i, value in enumerate(greater.menu_list):
                        qy2 = "INSERT INTO PLIST VALUES(?,?,?,?,?,?,?)"
                        __c.execute(qy2, ( count, greater.account_info[0], greater.menu_list[i], greater.price_list[i],
                                           greater.quantity_list[i], greater.agg_list[i], paydate))
                    # 결제 정보
                    qy3 = "INSERT INTO PAYINFO VALUES(?,?,?,?,?,?)"
                    __c.execute(qy3, (count, greater.account_info[0], number,
                                      self.lineEdit_inputmoney.text(), paydate, paytime))
                    ####################################################################################################
                    self.label_change.setText("{}원".format(int(self.lineEdit_inputmoney.text()) - int(number)))
                    self.label_order_info.setStyleSheet(
                        'QLabel{font: 75 12pt "맑은 고딕"; color: rgb(0, 112, 74); background-color: rgb(255, 255, 255);}')
                    self.label_order_info.setText("Thank you, have a good one!")
                    # 목록 초기화
                    row_number = self.tableWidget.rowCount()
                    for i in range(row_number):
                        self.tableWidget.removeRow(0)
                    self.lineEdit_inputmoney.clear()
                    greater.money = 0
                    self.label_total_money.setText("{}원".format(greater.money))
                    # 리스트 초기화
                    greater.menu_list.clear()
                    greater.price_list.clear()
                    greater.quantity_list.clear()
                    greater.agg_list.clear()
                else:
                    self.label_change.setText("{}원".format(int(self.lineEdit_inputmoney.text()) - int(number)))
                    self.label_order_info.setStyleSheet(
                        'QLabel{font: 75 12pt "맑은 고딕"; color: rgb(0, 112, 74);} background-color: rgb(255, 255, 255);')
                    self.label_order_info.setText("Thank you, have a good one!")
                    # 목록 초기화
                    row_number = self.tableWidget.rowCount()
                    for i in range(row_number):
                        self.tableWidget.removeRow(0)
                    self.lineEdit_inputmoney.clear()
                    greater.money = 0
                    self.label_total_money.setText("{}원".format(greater.money))
                    # 리스트 초기화
                    greater.menu_list.clear()
                    greater.price_list.clear()
                    greater.quantity_list.clear()
                    greater.agg_list.clear()
        except Exception as e:
            print(e)
            pass
    ####################################################################################################################
    ####################################################################################################################
    # my 페이지
    def account_update(self):
        self.lineEdit_check.clear()
        self.lineEdit_check.setStyleSheet(self.stylePopupOk)
        self.label_check_info.clear()
        self.stackedWidget_my.setCurrentWidget(self.page_check)

    def check_indicator(self, state, edit):
        if edit == self.lineEdit_check:
            self.label_check_info.clear()
            self.lineEdit_check.setStyleSheet(self.stylePopupOk)
        else:
            self.label_check_info2.clear()
            self.lineEdit_check2.setStyleSheet(self.stylePopupOk)

    def check(self):
        if greater.account_info[1] == self.lineEdit_check.text():
            self.stackedWidget_my.setCurrentWidget(self.page_account)
            self.label_account_id.setText(greater.account_info[0])
            self.lineEdit_account_pw.setText(greater.account_info[1])
            self.lineEdit_account_pw2.setText(greater.account_info[1])
            self.label_account_name.setText(greater.account_info[2])
            self.label_account_birth.setText(greater.account_info[3])
            self.lineEdit_account_phone.setText(greater.account_info[4])
            self.lineEdit_account_mail.setText(greater.account_info[5])
            self.lineEdit_account_nick.setText(greater.account_info[6])
            # indicator 처리
            self.label_account_info_1.clear()
            self.label_account_info_2.clear()
            self.label_account_info_pw.clear()
            self.lineEdit_account_pw.setStyleSheet(self.stylePopupOk)
            self.lineEdit_account_pw2.setStyleSheet(self.stylePopupOk)
            self.label_account_info_3.clear()
            self.label_account_info_3.clear()
            self.label_account_info_3.clear()
            self.label_account_info.clear()
            self.lineEdit_account_phone.setStyleSheet(self.stylePopupOk)
            self.lineEdit_account_mail.setStyleSheet(self.stylePopupOk)
            self.lineEdit_account_nick.setStyleSheet(self.stylePopupOk)
            #focus
            self.lineEdit_account_pw.setFocus()
            self.scrollArea_my.verticalScrollBar().setValue(0)
        else:
            self.label_check_info.setText("비밀번호가 틀렸습니다. 다시 입력해 주세요.")
            self.lineEdit_check.setStyleSheet(self.stylePopupError)
            self.lineEdit_check.clear()
    ####################################################################################################################
    ####################################################################################################################
    # 회원정보 수정
    def account_indicator(self, state, select):
        if select == self.lineEdit_account_pw:
            if len(self.lineEdit_account_pw.text()) < 10 or \
                    self.lineEdit_account_pw.text().isdigit() == True or\
                    self.lineEdit_account_pw.text().isalpha() == True or\
                    self.lineEdit_account_pw.text().isalnum() == False:
                self.label_account_info_1.setText('영문, 숫자 혼합하여 10~20자 이내로 입력해 주세요.')
                self.lineEdit_account_pw.setStyleSheet(self.stylePopupError)
            else:
                self.label_account_info_1.clear()
                self.lineEdit_account_pw.setStyleSheet(self.stylePopupOk)
                if self.lineEdit_account_pw2.text() != "" and\
                        self.lineEdit_account_pw.text() != self.lineEdit_account_pw2.text():
                    self.label_account_info_2.setText('비밀번호가 일치하지 않습니다.')
                    self.lineEdit_account_pw2.setStyleSheet(self.stylePopupError)
                else:
                    self.label_account_info_2.clear()
                    self.lineEdit_account_pw2.setStyleSheet(self.stylePopupOk)
        # 비번2
        elif select == self.lineEdit_account_pw2:
            if self.lineEdit_account_pw.text() != self.lineEdit_account_pw2.text():
                self.label_account_info_2.setText('비밀번호가 일치하지 않습니다.')
                self.lineEdit_account_pw2.setStyleSheet(self.stylePopupError)
            else:
                self.label_account_info_2.clear()
                self.lineEdit_account_pw2.setStyleSheet(self.stylePopupOk)
        # 번호
        elif select == self.lineEdit_account_phone:
            if 0 < len(self.lineEdit_account_phone.text()) < 11 or\
                    "010" not in self.lineEdit_account_phone.text() or\
                    self.lineEdit_account_phone.text().isdigit() == False:
                self.label_account_info_3.setText('"-"를 제외하고 번호 11자리를 입력해 주세요.')
                self.lineEdit_account_phone.setStyleSheet(self.stylePopupError)
            else:
                self.label_account_info_3.clear()
                self.lineEdit_account_phone.setStyleSheet(self.stylePopupOk)
        # 메일
        elif select == self.lineEdit_account_mail:
            if ("@" and ".") not in self.lineEdit_account_mail.text() or\
                    len(self.lineEdit_account_mail.text()) < 8:
                self.label_account_info_4.setText('이메일 형식이 아닙니다.')
                self.lineEdit_account_mail.setStyleSheet(self.stylePopupError)
            else:
                self.label_account_info_4.clear()
                self.lineEdit_account_mail.setStyleSheet(self.stylePopupOk)
        # 닉네임
        elif select == self.lineEdit_account_nick:
            hangeul = re.sub('[^가-힣]', "", self.lineEdit_account_nick.text())
            if len(hangeul) < 1 or len(hangeul) > 6:
                self.label_account_info_5.setText('한글 6자리 이내로 입력해 주세요.')
                self.lineEdit_account_nick.setStyleSheet(self.stylePopupError)
            else:
                self.label_account_info_5.clear()
                self.lineEdit_account_nick.setStyleSheet(self.stylePopupOk)

    def update_account(self, state, button):
        __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        __c = __connect.cursor()
        time = datetime.now()
        now = time.strftime('%Y-%m-%d/%H:%M:%S')
        if button == self.pushButton_account_update_pw:
            if self.lineEdit_account_pw.text() == greater.account_info[1] and \
                    self.lineEdit_account_pw2.text() == greater.account_info[1]:
                self.label_account_info_pw.setText("변경된 사항이 없습니다.")
            else: #if self.lineEdit_account_pw.text() != greater.account_info[1] and \
                    #self.lineEdit_account_pw2.text() != greater.account_info[1]:
                if self.label_account_info_1.text() == "" and\
                        self.label_account_info_2.text() == "":
                    greater.account_info[1] = self.lineEdit_account_pw.text()
                    qy = "UPDATE SMINFO SET (PW, RCP) = ('{}', '{}') WHERE ID = '{}'"
                    __c.execute(qy.format(greater.account_info[1], now, greater.account_info[0]))
                    self.stackedWidget_my.setCurrentWidget(self.page_account)
                    self.label_account_id.setText(greater.account_info[0])
                    self.lineEdit_account_pw.setText(greater.account_info[1])
                    self.lineEdit_account_pw2.setText(greater.account_info[1])
                    self.label_account_name.setText(greater.account_info[2])
                    self.label_account_birth.setText(greater.account_info[3])
                    self.lineEdit_account_phone.setText(greater.account_info[4])
                    self.lineEdit_account_mail.setText(greater.account_info[5])
                    self.lineEdit_account_nick.setText(greater.account_info[6])
                    self.checkBox_pw.setChecked(False)
                    self.lineEdit_account_pw.setEchoMode(QLineEdit.Password)
                    self.checkBox_pw2.setChecked(False)
                    self.lineEdit_account_pw2.setEchoMode(QLineEdit.Password)
                    self.label_account_info_pw.setText('비밀번호가 변경 되었습니다.')
        else:
            if self.lineEdit_account_phone.text() == greater.account_info[4] and\
                    self.lineEdit_account_mail.text() == greater.account_info[5] and\
                    self.lineEdit_account_nick.text() == greater.account_info[6]:
                self.label_account_info.setText('변경된 사항이 없습니다.')
            else:
                if self.label_account_info_3.text() == "" and\
                        self.label_account_info_4.text() == "" and\
                        self.label_account_info_5.text() == "":
                    greater.account_info[4] = self.lineEdit_account_phone.text()
                    greater.account_info[5] = self.lineEdit_account_mail.text()
                    greater.account_info[6] = self.lineEdit_account_nick.text()
                    print(greater.account_info[4])
                    print(greater.account_info[5])
                    print(greater.account_info[6])
                    qy = "UPDATE SMINFO SET (PHONE, EMAIL, NICK) = ('{}', '{}', '{}') WHERE ID = '{}'"
                    __c.execute(qy.format(greater.account_info[4], greater.account_info[5],
                                          greater.account_info[6], greater.account_info[0]))
                    ...
                    self.stackedWidget_my.setCurrentWidget(self.page_account)
                    self.label_account_id.setText(greater.account_info[0])
                    self.lineEdit_account_pw.setText(greater.account_info[1])
                    self.lineEdit_account_pw2.setText(greater.account_info[1])
                    self.label_account_name.setText(greater.account_info[2])
                    self.label_account_birth.setText(greater.account_info[3])
                    self.lineEdit_account_phone.setText(greater.account_info[4])
                    self.lineEdit_account_mail.setText(greater.account_info[5])
                    self.lineEdit_account_nick.setText(greater.account_info[6])
                    self.label_account_info.setText('회원정보가 수정 되었습니다.')

    def account_checkbox(self, state, clicked):
        if clicked == self.checkBox_pw:
            if self.checkBox_pw.isChecked() == True:
                self.lineEdit_account_pw.setEchoMode(QLineEdit.Normal)
            else:
                self.lineEdit_account_pw.setEchoMode(QLineEdit.Password)
        else:
            if self.checkBox_pw2.isChecked() == True:
                self.lineEdit_account_pw2.setEchoMode(QLineEdit.Normal)
            else:
                self.lineEdit_account_pw2.setEchoMode(QLineEdit.Password)
    ####################################################################################################################
    ####################################################################################################################
    # 회원탈퇴
    def account_close(self):
        self.checkBox_account_close.setChecked(False)
        self.label_account_close_info2.clear()
        self.stackedWidget_my.setCurrentWidget(self.page_close)

    def close_checkbox(self):
        if self.checkBox_account_close.isChecked() == True:
            self.label_account_close_info2.clear()

    def close_account(self):
        if self.checkBox_account_close.isChecked() == True:
            self.lineEdit_check2.clear()
            self.lineEdit_check2.setStyleSheet(self.stylePopupOk)
            self.label_check_info2.clear()
            self.stackedWidget_my.setCurrentWidget(self.page_check2)
        else:
            self.label_account_close_info2.setText("동의가 필요합니다.")

    def check2(self):
        print(greater.account_info[0])
        print(greater.account_info[1])
        __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        __c = __connect.cursor()
        if greater.account_info[1] == self.lineEdit_check2.text():
            self.lineEdit_check2.clear()
            self.pushButton_my.setEnabled(False)
            self.pushButton_my.setText("")
            self.pushButton_logout.setEnabled(False)
            self.pushButton_logout.setText("")
            self.label_top.clear()
            self.pushButton_login.setEnabled(True)
            self.pushButton_login.setText("로그인")
            qy = "DELETE FROM SMINFO WHERE ID ='{}'"
            __c.execute(qy.format(greater.account_info[0]))
            qy = "DELETE FROM PLIST WHERE ID ='{}'"
            __c.execute(qy.format(greater.account_info[0]))
            qy = "DELETE FROM PAYINFO WHERE ID ='{}'"
            __c.execute(qy.format(greater.account_info[0]))
            greater.account_info.clear()
            self.stackedWidget.setCurrentWidget(self.page_close_end)
        else:
            self.label_check_info2.setText("비밀번호가 틀렸습니다. 다시 입력해 주세요.")
            self.lineEdit_check2.setStyleSheet(self.stylePopupError)
    ####################################################################################################################
    ####################################################################################################################
    # 로그아웃
    def logout(self):
        greater.account_info.clear()
        self.pushButton_my.setEnabled(False)
        self.pushButton_my.setText("")
        self.pushButton_logout.setEnabled(False)
        self.pushButton_logout.setText("")
        self.label_top.clear()
        self.pushButton_login.setEnabled(True)
        self.pushButton_login.setText("로그인")
        self.stackedWidget.setCurrentWidget(self.page_start)
    ####################################################################################################################
    ####################################################################################################################
    # 구매내역 조회
    def purchase_list(self):
        self.listWidget.clear()
        print("test")
        id = greater.account_info[0]
        year = self.comboBox_list_1.currentText()
        month = self.comboBox_list_2.currentText()
        day = self.comboBox_list_3.currentText()
        print(self.comboBox_list_1.currentText())
        __connect = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        __c = __connect.cursor()
        qy1 = """
        SELECT COUNT(PAYDATE)
        FROM SMINFO A JOIN PAYINFO B ON A.ID = B.ID
        WHERE A.ID = '{}' AND PAYDATE = '{}/{}/{}'
        """
        __c.execute(qy1.format(id, year, month, day))
        iy = __c.fetchone()
        print(iy)
        print(type(iy[0]))
        # repeat = 0
        if iy[0] == 0:
            repeat = 0
            text = '구매내역이 없습니다.'
            item = QListWidgetItem(text)
            item.setTextAlignment(Qt.AlignCenter)
            self.listWidget.addItem(item)
        else:
            repeat = iy[0]
        print(repeat)
        for i in range(repeat):
            qy2 = """
            SELECT PAYDATE, PAYTIME, AMOUNT, PAY
            FROM SMINFO A JOIN PAYINFO B ON A.ID = B.ID
            WHERE B.ID = '{}' AND PAYDATE = '{}/{}/{}'
            ORDER BY PAYTIME
            """
            __c.execute(qy2.format(id, year, month, day))
            iy2 = __c.fetchall()
            payinfo = iy2[i]
            print(payinfo[0], payinfo[1])
            text1 = '|| 구매일자 : {} || 구매시간 : {} ||'.format(payinfo[0], payinfo[1])
            item1 = QListWidgetItem(text1)
            item1.setTextAlignment(Qt.AlignCenter)
            font = item1.font()
            font.setPointSize(13)
            item1.setFont(font)
            self.listWidget.addItem(item1)

            qy3 = """
            SELECT MENU, PRICE, PCS, AGG
            FROM PAYINFO A JOIN PLIST B
            ON A.ODNO = B.ODNO AND A.ID = B.ID AND A.PAYDATE = B.PAYDATE
            WHERE B.ID = '{}' AND B.PAYDATE = '{}/{}/{}' AND B.ODNO = '{}'
            """
            __c.execute(qy3.format(id, year, month, day, i))
            iy3 = __c.fetchall()
            for j in range(len(iy3)):
                print(iy3[j])
                plist = iy3[j]
                text2 = '{} ￦{} / {}개 / {}원'.format(plist[0], plist[1], plist[2], plist[3])
                item2 = QListWidgetItem(text2)
                item2.setTextAlignment(Qt.AlignRight)
                self.listWidget.addItem(item2)
            ...
            print(payinfo[2], payinfo[3])
            text3 = '결제할 금액: {}원\n지불한 금액: {}원'.format(payinfo[2], payinfo[3])
            item3 = QListWidgetItem(text3)
            item3.setTextAlignment(Qt.AlignRight)
            self.listWidget.addItem(item3)
            self.listWidget.addItem(" ")

    def clear_list(self, steat, button):
        if button == self.pushButton_my:
            self.listWidget.clear()
            self.stackedWidget.setCurrentWidget(self.page_my)
            self.stackedWidget_my.setCurrentWidget(self.page_list)
        else:
            self.listWidget.clear()
            self.stackedWidget_my.setCurrentWidget(self.page_list)
    ####################################################################################################################
    ####################################################################################################################
    # 마우스
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.offset = event.pos()
        else:
            super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)
    ####################################################################################################################
    ####################################################################################################################
    # 종료
    def windowclose(self):
        ch.close()

app = QApplication(sys.argv)
ch = window()
ch.show()
app.exec_()