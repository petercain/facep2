import sys, re, webbrowser, sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from datetime import *

page1 = "star1.ui"
page2 = "star2.ui"
page3 = "star3.ui"
page4 = "star4.ui"
page5 = "star_kiosk.ui"

class greater:
    my_acoount_info = []

    # total_money = 0
    #
    # # 메뉴 가격 리스트
    # menu_list = []
    # price_list = []

class variable:
    total_money = 0
    # 메뉴 가격 리스트
    menu_list = []
    price_list = []
########################################################################################################################
# page 1
########################################################################################################################
class Page1(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page1, self)

        self.pb_Login.clicked.connect(self.login)
        self.pb_Join.clicked.connect(self.join)

    def join(self):
        self.Page2 = Page2()
        self.Page2.show()
        self.close()

    def login(self):
        conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT * FROM MEMBERSHIP WHERE ID = '{}'".format(self.lineEdit_id.text()))
        result = cur.fetchone()
        print(result)
        if result == None:
            QMessageBox.critical(self, " ", "계정 혹은 비밀번호가 일치하지 않습니다.")
        else:
            for row in result:
                print(row)
                greater.my_acoount_info.append(row)
                print(greater.my_acoount_info)

            if greater.my_acoount_info[1] == self.lineEdit_pw.text():
                self.page3 = Page3()
                self.page3.show()
                self.close()
            else:
                greater.my_acoount_info.clear()
                QMessageBox.information(self, " ", "계정 혹은 비밀번호가 일치하지 않습니다.", QMessageBox.Ok)
########################################################################################################################
# page 2 회원가입
########################################################################################################################
class Page2(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page2, self)

        self.next_check = []

        self.pb_check.clicked.connect(self.click)
        self.pb_next.clicked.connect(self.next)
        self.pb_cancel.clicked.connect(self.cancel)
        # 아이디 입력란 수정시 시그널
        self.lineEdit.textEdited.connect(self.text_edited)

# 중복 체크
    def click(self):
        conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
        cur = conn.cursor()
        cur.execute("SELECT ID FROM MEMBERSHIP WHERE ID = '{}'".format(self.lineEdit.text()))
        result = cur.fetchall()
        id_list = []
        for row in result:
            id_list.append(row)


        if  self.lineEdit.text() in id_list:
            QMessageBox.critical(self, " ", "중복된 아이디입니다.")
        else:
            check = QMessageBox.information(self, " ", "사용 가능한 아이디입니다.")
            if check == QMessageBox.Ok:
                print(111111)
                self.next_check.append("yes")
                print(self.next_check)

    def text_edited(self):
        self.next_check.clear()
        print(self.next_check)

    def next(self):
        if "yes" not in self.next_check:
            QMessageBox.information(self, " ", "아이디 중복 확인을 해주세요.")
        elif len(self.lineEdit.text()) < 5:
            QMessageBox.critical(self, " ", "아이디를 최소 5 이상 입력해주세요.")
        elif len(self.lineEdit_2.text()) < 8:
            QMessageBox.critical(self, " ", "비밀번호를 최소 8 이상 입력해주세요.")
        elif len(self.lineEdit_3.text()) < 1:
            QMessageBox.critical(self, " ", "닉네임를 최소 한글자 이상 입력해주세요.")
        else:
            id = self.lineEdit.text()
            pw = self.lineEdit_2.text()
            nick = self.lineEdit_3.text()
            conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("insert into MEMBERSHIP values(?,?,?)", (id, pw, nick))
            self.page = Page1()
            self.page.show()
            self.close()

    def cancel(self):
        Pg.show()
        self.close()

########################################################################################################################
# page 3
########################################################################################################################
class Page3(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page3, self)

        self.pb_membership.clicked.connect(self.membership)
        self.pb_home.clicked.connect(self.home)
        self.pb_remove.clicked.connect(self.remove)
        self.pb_check.clicked.connect(self.check)
        self.label_confirm.setText("{} 님, Welcome to Starbucks".format(greater.my_acoount_info[0]))

    def check(self):
        year = re.findall(r'\d+', self.comboBox_year.currentText())
        year = year[0]
        # print(year)
        month = re.findall(r'\d+', self.comboBox_month.currentText())
        month = month[0]
        # print(month)
        day = re.findall(r'\d+', self.comboBox_day.currentText())
        day = day[0]
        # print(day)
        try:
            conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            cur = conn.cursor()
            qy1 = """
            SELECT MAX(NUMBER) FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}'
            """
            cur.execute(qy1.format(greater.my_acoount_info[0], year, month, day))
            number = cur.fetchone() # 예시 [(5, 3), (3, 4), (1, 2)] // cur.fetchone() # (5, 3)
            print(number[0])
            if number[0] == None:
                count = None
                pass
            else:
                count = int(number[0]) + 1
            print(count)
        except Exception as e:
            print(e)
            pass
        try:
            for i in range(count):
                qy2 = """
                SELECT TOTAL, PAYDATE, PAYTIME FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}'
                """
                cur.execute(qy2.format(greater.my_acoount_info[0], year, month, day))
                result_1 = cur.fetchall()
                print(result_1)
                total, date, time = zip(*result_1)
                list_total = list(dict.fromkeys(total))
                list_date = list(dict.fromkeys(date))
                list_time = list(dict.fromkeys(time))
                print(list_total)
                print(list_date)
                print(list_time)
                self.textBrowser.append('{} ★ {}'.format(list_date[0], list_time[i]))

                qy3 = """
                SELECT MENU, PRICE FROM ORDERDETAILE WHERE ID = '{}' AND PAYDATE = '{}.{}.{}' and NUMBER = '{}'
                """
                cur.execute(qy3.format(greater.my_acoount_info[0], year, month, day, i))
                result_2 = cur.fetchall()
                print(result_2)
                for j in range(len(result_2)):
                    menu = result_2[j]
                    self.textBrowser.append('{} ￦{}'.format(menu[0], menu[1]))
                self.textBrowser.append('TOTAL ￦{}'.format(list_total[i]))
                self.textBrowser.append("")
        except Exception as e:
            print(e)
            pass








        #print(result)
        # list_total_time = []
        # for i in result_1:
        #     for j in i:
        #         print(j)
        #         list_total_time.append(j)
        # print(list_total_time)
        # # og = list(set(list_total_time)) # 그냥 중복제거(순서 유지 x)
        # # print(og)
        # og = list(dict.fromkeys(list_total_time)) # 중복제거(순서 유지)
        # print(og)
        # total, time = zip(*result_1)
        # print(list(dict.fromkeys(total)))
        # print(list(dict.fromkeys(time)))
        # list_total = list(dict.fromkeys(total))
        # list_time = list(dict.fromkeys(time))
        # cur.execute("SELECT MENU, PRICE FROM ORDERDETAILE WHERE ID = '{}'".format(greater.my_acoount_info[0]))
        # result_2 = cur.fetchall() # [(5, 3), (3, 4), (1, 2)]
        # for x, value in enumerate(list_time):
        #     self.textBrowser.append(list_time[x])
        #     for y in result_2:
        #         print(x)
        #         self.textBrowser.append(y[0] + "  ￦" + y[1]) # (허니 자몽 블랙티, 5800)
        #     self.textBrowser.append(list_total[x])

    def remove(self):
        remove = QMessageBox.information(self, " ", "{} 님 정말 탈퇴하시겠습니까?".format(greater.my_acoount_info[0]), QMessageBox.No | QMessageBox.Yes, QMessageBox.No)
        if remove == QMessageBox.Yes:
            conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            cur = conn.cursor()
            cur.execute("delete FROM MEMBERSHIP WHERE ID = '{}'".format(greater.my_acoount_info[0]))
            greater.my_acoount_info.clear()
            Pg.show()
            self.close()
        else:
            pass

    def home(self):
        self.dorothy = Page5()
        self.dorothy.show()
        self.close()

    def membership(self):
        self.dorothy = Page4()
        self.dorothy.show()
        self.close()

    def display(self):
        self.show()

########################################################################################################################
# page 4
########################################################################################################################
class Page4(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page4, self)

        self.pb_cancel.clicked.connect(self.cancel)
        self.pb_confirm.clicked.connect(self.confirm)
        self.label.setText(greater.my_acoount_info[0])

    def cancel(self):
        self.dorothy = Page3()
        self.dorothy.show()
        self.close()

    def confirm(self):
        if greater.my_acoount_info[1] == self.lineEdit_mi1.text():
            conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            cur = conn.cursor()
            pw = self.lineEdit_mi2.text()
            nick = self.lineEdit_mi3.text()
            cur.execute("UPDATE MEMBERSHIP SET (PASSWORD, NICKNAME) = ('{}', '{}') where ID = '{}'".format(pw, nick, greater.my_acoount_info[0]))
            greater.my_acoount_info[1] = pw
            greater.my_acoount_info[2] = nick
            print(greater.my_acoount_info)
            check = QMessageBox.information(self, " ", "회원정보가 변경되었습니다.", QMessageBox.Ok)
            if check == QMessageBox.Ok:
                self.dorothy = Page3()
                self.dorothy.show()
                self.close()
########################################################################################################################
# page 5
########################################################################################################################
class Page5(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None, Qt.WindowStaysOnTopHint)
        uic.loadUi(page5, self)
        self.setWindowTitle('Starbucks')
        self.setGeometry(800, 800, 800, 800)

        # 버튼에 링크 추가하기
        self.new_btn.clicked.connect(lambda: webbrowser.open('https://www.starbucks.co.kr/whats_new/index.do'))
        self.summer_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/whats_new/campaign_view.do?pro_seq=1864'))
        self.reward_btn.clicked.connect(
            lambda: webbrowser.open('https://www.starbucks.co.kr/msr/msreward/level_benefit.do'))

        ###next 버튼 실행시 페이지 전환
        self.Btn_pay_next1.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_pay2))
        self.Btn_pay_next2.clicked.connect(self.pay_succeed)

        # 첫 페이지 설정
        ### 홈
        self.tabWidget.setCurrentWidget(self.tab_home)
        ### 음료
        self.tabWidget_drink_and_food.setCurrentWidget(self.tab_drink)
        ### 음료 & 푸드 new
        self.tool_drink.setCurrentWidget(self.page_drink_new)
        self.tool_food.setCurrentWidget(self.page_food_new)
        ### 결제
        self.stackedWidget.setCurrentWidget(self.page_pay1)

        #결제 창 리셋 시그널 준 부분
        self.tabWidget.currentChanged.connect(self.reset)

        # self.Btn_next4.clicked.connect(self.next_tab3)
        # self.Btn_next5.clicked.connect(self.next_tab3)
        # self.Btn_cancel1.clicked.connect(self.prev_tab2)
        # self.Btn_cancel1.clicked.connect(self.btsclear)
        # self.Btn_close.clicked.connect(QCoreApplication.instance().quit)
        
        ##버튼 1-58번
        self.Btn_1.clicked.connect(lambda : self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_2.clicked.connect(lambda : self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_3.clicked.connect(lambda : self.tabWidget.setCurrentWidget(self.tab_pay))
        self.Btn_4.clicked.connect(lambda : self.tabWidget.setCurrentWidget(self.tab_pay))

        self.Btn_1.clicked.connect(lambda state, button = self.Btn_1, price = 3800, menu = "오늘의 커피" : self.add_menu(state, button, price, menu))
        self.Btn_2.clicked.connect(lambda state, button = self.Btn_2, price = 5800, menu = "허니 자몽 블랙티" : self.add_menu(state, button, price, menu))
        self.Btn_3.clicked.connect(lambda state, button = self.Btn_3, price = 6300, menu = "유기농 말차 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_4.clicked.connect(lambda state, button = self.Btn_4, price = 4100, menu = "아메리카노" : self.add_menu(state, button, price, menu))
        self.Btn_5.clicked.connect(lambda state, button = self.Btn_5, price = 8300, menu = "루비레드 칠링 아이스티" : self.add_menu(state, button, price, menu))
        self.Btn_6.clicked.connect(lambda state, button = self.Btn_6, price = 8600, menu = "제스트 그린 블랜디드" : self.add_menu(state, button, price, menu))
        self.Btn_7.clicked.connect(lambda state, button = self.Btn_7, price = 8500, menu = "루프탑 그레이 라떼" : self.add_menu(state, button, price, menu))
        self.Btn_8.clicked.connect(lambda state, button = self.Btn_8, price = 6600, menu = "아이스크림 블랜딩 콜드브루" : self.add_menu(state, button, price, menu))
        self.Btn_9.clicked.connect(lambda state, button = self.Btn_9, price = 5900, menu = "아이스 유자 & 유자베리 티" : self.add_menu(state, button, price, menu))
        self.Btn_10.clicked.connect(lambda state, button = self.Btn_10, price = 6300, menu = "트윙클 스타 핑크 블랜디드" : self.add_menu(state, button, price, menu))
        self.Btn_11.clicked.connect(lambda state, button = self.Btn_11, price = 7500, menu = "제주까망 크림 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_12.clicked.connect(lambda state, button = self.Btn_12, price = 7500, menu = "쑥떡 크림 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_13.clicked.connect(lambda state, button = self.Btn_13, price = 7500, menu = "별다방 땅콩 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_14.clicked.connect(lambda state, button = self.Btn_14, price = 7500, menu = "천혜향 블랙티 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_15.clicked.connect(lambda state, button = self.Btn_15, price = 7000, menu = "제주 청귤 레모네이드" : self.add_menu(state, button, price, menu))
        self.Btn_16.clicked.connect(lambda state, button = self.Btn_16, price = 7200, menu = "별다방 땅콩 라뗴" : self.add_menu(state, button, price, menu))
        self.Btn_17.clicked.connect(lambda state, button = self.Btn_17, price = 4100, menu = "아메리카노" : self.add_menu(state, button, price, menu))
        self.Btn_18.clicked.connect(lambda state, button = self.Btn_18, price = 4600, menu = "카페 라떼" : self.add_menu(state, button, price, menu))
        self.Btn_19.clicked.connect(lambda state, button = self.Btn_19, price = 5100, menu = "카페 모카" : self.add_menu(state, button, price, menu))
        self.Btn_20.clicked.connect(lambda state, button = self.Btn_20, price = 5600, menu = "들체 라떼" : self.add_menu(state, button, price, menu))
        self.Btn_21.clicked.connect(lambda state, button = self.Btn_21, price = 5600, menu = "바닐라 플랫 화이트" : self.add_menu(state, button, price, menu))
        self.Btn_22.clicked.connect(lambda state, button = self.Btn_22, price = 4400, menu = "디카페인 아메리카노" : self.add_menu(state, button, price, menu))
        self.Btn_23.clicked.connect(lambda state, button = self.Btn_23, price = 6300, menu = "유기농 말차 크림 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_24.clicked.connect(lambda state, button = self.Btn_24, price = 6100, menu = "자바칩 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_25.clicked.connect(lambda state, button = self.Btn_25, price = 6500, menu = "화이트 타이거 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_26.clicked.connect(lambda state, button = self.Btn_26, price = 5600, menu = "카라멜 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_27.clicked.connect(lambda state, button = self.Btn_27, price = 6100, menu = "화이트 딸기 크림 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_28.clicked.connect(lambda state, button = self.Btn_28, price = 5600, menu = "모카 프라푸치노" : self.add_menu(state, button, price, menu))
        self.Btn_29.clicked.connect(lambda state, button = self.Btn_29, price = 6100, menu = "민트 초콜릿칩 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_30.clicked.connect(lambda state, button = self.Btn_30, price = 6100, menu = "딸기 딜라이트 요거트 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_31.clicked.connect(lambda state, button = self.Btn_31, price = 6300, menu = "망고 바나나 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_32.clicked.connect(lambda state, button = self.Btn_32, price = 5000, menu = "망고 패션 프루트 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_33.clicked.connect(lambda state, button = self.Btn_33, price = 8600, menu = "제스트 그린 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_34.clicked.connect(lambda state, button = self.Btn_34, price = 6300, menu = "트윙클 스타 핑크 블렌디드" : self.add_menu(state, button, price, menu))
        self.Btn_35.clicked.connect(lambda state, button = self.Btn_35, price = 6900, menu = "블루베리 치즈 케이크" : self.add_menu(state, button, price, menu))
        self.Btn_36.clicked.connect(lambda state, button = self.Btn_36, price = 3500, menu = "헤이즐럿 브라우니" : self.add_menu(state, button, price, menu))
        self.Btn_37.clicked.connect(lambda state, button = self.Btn_37, price = 4500, menu = "밤콩 달콩 두유 브레드" : self.add_menu(state, button, price, menu))
        self.Btn_38.clicked.connect(lambda state, button = self.Btn_38, price = 7900, menu = "샤인 머스캣 스위박스" : self.add_menu(state, button, price, menu))
        self.Btn_39.clicked.connect(lambda state, button = self.Btn_39, price = 7500, menu = "(제주) 녹차 생크림 롤" : self.add_menu(state, button, price, menu))
        self.Btn_40.clicked.connect(lambda state, button = self.Btn_40, price = 7800, menu = "돌코롱 쫍지롱 와플샌드" : self.add_menu(state, button, price, menu))
        self.Btn_41.clicked.connect(lambda state, button = self.Btn_41, price = 4900, menu = "베이컨 치즈 토스트" : self.add_menu(state, button, price, menu))
        self.Btn_42.clicked.connect(lambda state, button = self.Btn_42, price = 6200, menu = "리코타 치즈 바게트 샌드" : self.add_menu(state, button, price, menu))
        self.Btn_43.clicked.connect(lambda state, button = self.Btn_43, price = 5800, menu = "바베큐 치킨 치즈 치아바타" : self.add_menu(state, button, price, menu))
        self.Btn_44.clicked.connect(lambda state, button = self.Btn_44, price = 5200, menu = "트리플 치즈 크로크 무슈" : self.add_menu(state, button, price, menu))
        self.Btn_45.clicked.connect(lambda state, button = self.Btn_45, price = 4500, menu = "부드러운 생크림 카스텔라" : self.add_menu(state, button, price, menu))
        self.Btn_46.clicked.connect(lambda state, button = self.Btn_46, price = 5900, menu = "튜나 멜트 샌드위치" : self.add_menu(state, button, price, menu))
        self.Btn_47.clicked.connect(lambda state, button = self.Btn_47, price = 3000, menu = "리얼 블루베리 베이글" : self.add_menu(state, button, price, menu))
        self.Btn_48.clicked.connect(lambda state, button = self.Btn_48, price = 3300, menu = "클래식 스콘" : self.add_menu(state, button, price, menu))
        self.Btn_49.clicked.connect(lambda state, button = self.Btn_49, price = 4300, menu = "연유 밀크모닝" : self.add_menu(state, button, price, menu))
        self.Btn_50.clicked.connect(lambda state, button = self.Btn_50, price = 3200, menu = "프렌치 크로아상" : self.add_menu(state, button, price, menu))
        self.Btn_51.clicked.connect(lambda state, button = self.Btn_51, price = 4900, menu = "(제주)앙녹차 베이글" : self.add_menu(state, button, price, menu))
        self.Btn_52.clicked.connect(lambda state, button = self.Btn_52, price = 4900, menu = "우유를 품은 초콜릿 크로와상" : self.add_menu(state, button, price, menu))
        self.Btn_53.clicked.connect(lambda state, button = self.Btn_53, price = 5900, menu = "부드러운 티라미수 롤" : self.add_menu(state, button, price, menu))
        self.Btn_54.clicked.connect(lambda state, button = self.Btn_54, price = 5700, menu = "진한 녹차 생크림 케이크" : self.add_menu(state, button, price, menu))
        self.Btn_55.clicked.connect(lambda state, button = self.Btn_55, price = 6900, menu = "번트 치즈 케이크" : self.add_menu(state, button, price, menu))
        self.Btn_56.clicked.connect(lambda state, button = self.Btn_56, price = 5500, menu = "레드 벨벳 크림치즈 케이크" : self.add_menu(state, button, price, menu))
        self.Btn_57.clicked.connect(lambda state, button = self.Btn_57, price = 6800, menu = "당근 현무암케이크" : self.add_menu(state, button, price, menu))
        self.Btn_58.clicked.connect(lambda state, button = self.Btn_58, price = 6500, menu = "새코롬 돌코롬 한라봉 케이크" : self.add_menu(state, button, price, menu))

        ## 결제부분에서 취소
        self.Btn_cancel1.clicked.connect(self.cancel_menu)
        self.Btn_cancel2.clicked.connect(self.cancel_menu)

        # 결제 끝에서 close버튼
        self.Btn_close.clicked.connect(self.end)

# 테이블에 메뉴 상품명, 상품에 대한 가격, 총 주문한 상품의 가격(결제할 총 금액)
    def add_menu(self, state, button, price, menu):
        self.textBrowser.append("{} {}원이 추가 되었습니다.".format(menu, price))
        print(menu)
        variable.total_money += price
        variable.menu_list.append(menu)
        variable.price_list.append(price)
        self.total_money1.setText("{}".format(variable.total_money))
        self.total_money2.setText("{}".format(variable.total_money))
        print(variable.menu_list)
        print(variable.price_list)

    def reset(self):
        self.stackedWidget.setCurrentWidget(self.page_pay1)

    def cancel_menu(self):
        variable.total_money = 0
        variable.menu_list.clear()
        variable.price_list.clear()
        print(variable.menu_list)
        print(variable.price_list)
        self.total_money1.clear()
        self.total_money2.clear()
        self.textBrowser.clear()
        self.tabWidget.setCurrentWidget(self.tab_home)

    def pay_succeed(self):
        try:
            time = datetime.now()
            paydate = time.strftime("%Y.%m.%d")
            paytime = time.strftime("%H:%M:%S")
            conn = sqlite3.connect("STARBUCKS.db", isolation_level=None)
            cur = conn.cursor()

            qy1 = """
                    SELECT MAX(NUMBER) FROM ORDERDETAILE
                    WHERE ID = '{}' AND PAYDATE = STRFTIME('%Y.%m.%d', 'now', 'localtime')
                    """
            cur.execute(qy1.format(greater.my_acoount_info[0]))
            iy = cur.fetchone()
            print(iy[0])
            if iy[0] == None:
                number = 0
            else:
                number = int(iy[0]) + 1

            for i, value in enumerate(variable.menu_list):  # 메뉴와 가격이 같이 들어가기 때문에 둘 중 하나만 넣어도 됨
                qy = "INSERT INTO ORDERDETAILE VALUES(?,?,?,?,?,?,?)"
                cur.execute(qy, (
                greater.my_acoount_info[0], variable.menu_list[i], variable.price_list[i], variable.total_money,
                paydate, paytime, number))
            # db테이블에 데이터를 넣을 때 - for문 활용하기(리스트이기 때문에) for i, value in enumerate(variable):
            self.stackedWidget.setCurrentWidget(self.page_pay3)
            variable.total_money = 0
            self.total_money1.clear()
            self.total_money2.clear()
            self.textBrowser.clear()
        except Exception as e:
            print(e)
            pass
    def end(self):
        self.page3 = Page3()
        self.page3.display()
        self.close()
########################################################################################################################
########################################################################################################################
app = QApplication(sys.argv)
Pg = Page1()
Pg.show()
app.exec_()
