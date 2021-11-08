import sys, re
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from random import *
########################################################################################################################
########################################################################################################################
UI1 = '../_qt_ui/pokemon1_1.ui'
UI2 = '../_qt_ui/pokemon2_1.ui'
UI3 = '../_qt_ui/pokemon3.ui'
UI_potion = '../_qt_ui/pokemon_potion.ui'
UI4 = '../_qt_ui/pokemon4.ui'
########################################################################################################################
########################################################################################################################
class variable_value:
    my_name = []
    page3_level = []
    minimum_hpmp = 0
    my_hp = 100
    my_mp = 100
    maximum_ex = 100
    experience_value = 0
    hp_potion = 0
    mp_potion = 0
    game_money = 0
    my_level = [["Lv. 1 피카츄", "Lv. 2 피카츄", "Lv. 3 피카츄", "Lv. 4 피카츄"],
                ["Lv. 1 파이리", "Lv. 2 리자드", "Lv. 3 리자드", "Lv. 4 리자몽"],
                ["Lv. 1 꼬부기", "Lv. 2 어니부기", "Lv. 3 어니부기", "Lv. 4 거북왕"],
                ["Lv. 1 이상해씨", "Lv. 2 이상해풀", "Lv. 3 이상해풀", "Lv. 4 이상해꽃"]]
    # [0] ~ 0
    # [4] ~ 4 5 7
    # [8] ~ 8 9 11
    # [12] ~ 12 13 15
    ex = randint(299, 300)
    gm = randint(10, 100)
    ta = randint(5, 15)
    # 17820
    level1_ex = 0
    level2_ex = 0
    level3_ex = 0
    level4_ex = 0
########################################################################################################################
class oppsing:
    op1 = '../_qt_ui/poke/op/1/op1.gif'
    op2 = '../_qt_ui/poke/op/1/op2.gif'
    op3 = '../_qt_ui/poke/op/1/op3.gif'
    op4 = '../_qt_ui/poke/op/2/op1.gif'
    op5 = '../_qt_ui/poke/op/2/op2.gif'
    op6 = '../_qt_ui/poke/op/2/op3.gif'
    op7 = '../_qt_ui/poke/op/2/op4.gif'
    op8 = '../_qt_ui/poke/op/2/op5.gif'
    op9 = '../_qt_ui/poke/op/3/op1.gif'
    op10 = '../_qt_ui/poke/op/3/op2.gif'
    op11 = '../_qt_ui/poke/op/3/op3.gif'
    op12 = '../_qt_ui/poke/op/3/op4.gif'
    op13 = '../_qt_ui/poke/op/3/op5.gif'
    op14 = '../_qt_ui/poke/op/3/op6.gif'
    op15 = '../_qt_ui/poke/op/3/op7.gif'
    op16 = '../_qt_ui/poke/op/3/op8.gif'
    op17 = '../_qt_ui/poke/op/3/op9.gif'
    op18 = '../_qt_ui/poke/op/3/op10.gif'
    op19 = '../_qt_ui/poke/op/4/op1.gif'
    op20 = '../_qt_ui/poke/op/4/op2.gif'
    op21 = '../_qt_ui/poke/op/4/op3.gif'
    op22 = '../_qt_ui/poke/op/4/op4.gif'
    op23 = '../_qt_ui/poke/op/4/op5.gif'
    op24 = '../_qt_ui/poke/op/4/op6.gif'
    op25 = '../_qt_ui/poke/op/4/op7.gif'
    op26 = '../_qt_ui/poke/op/4/op8.gif'
    op27 = '../_qt_ui/poke/op/4/op9.gif'
    op28 = '../_qt_ui/poke/op/4/op10.gif'
    op29 = '../_qt_ui/poke/op/5/op1.gif'
    op30 = '../_qt_ui/poke/op/5/op2.gif'
    op31 = '../_qt_ui/poke/op/5/op3.gif'
    op32 = '../_qt_ui/poke/op/5/op4.gif'
    op33 = '../_qt_ui/poke/op/5/op5.gif'
    op34 = '../_qt_ui/poke/op/5/op6.gif'
    op35 = '../_qt_ui/poke/op/5/op7.gif'
    op36 = '../_qt_ui/poke/op/5/op8.gif'
    op37 = '../_qt_ui/poke/op/5/op9.gif'
    op38 = '../_qt_ui/poke/op/5/op10.gif'
    op_list = [op1, op2, op3, op4, op5, op6, op7, op8, op9, op10, op11, op12, op13, op14, op15, \
               op16, op17, op18, op19, op20, op21, op22, op23, op24, op25, op26, op27, op28, op29, op30, \
               op31, op32, op33, op34, op35, op36, op37, op38]
########################################################################################################################
class gif:
    def ppp(self):
        p1 = QMovie("../_qt_ui/poke/p/p1.gif")
        self.poke3.label_pokemon1.setMovie(p1)
        p1.start()
        p2 = QMovie("../_qt_ui/poke/p/p2.gif")
        self.poke3.label_pokemon2.setMovie(p2)
        p2.start()
        p3 = QMovie("../_qt_ui/poke/p/p3.gif")
        self.poke3.label_pokemon3.setMovie(p3)
        p3.start()

    def fff(self):
        f1 = QMovie("../_qt_ui/poke/f/f1.gif")
        self.poke3.label_pokemon1.setMovie(f1)
        f1.start()
        f2 = QMovie("../_qt_ui/poke/f/f2.gif")
        self.poke3.label_pokemon2.setMovie(f2)
        f2.start()
        f3 = QMovie("../_qt_ui/poke/f/f3.gif")
        self.poke3.label_pokemon3.setMovie(f3)
        f3.start()

    def kkk(self):
        k1 = QMovie("../_qt_ui/poke/k/k1.gif")
        self.poke3.label_pokemon1.setMovie(k1)
        k1.start()
        k2 = QMovie("../_qt_ui/poke/k/k2.gif")
        self.poke3.label_pokemon2.setMovie(k2)
        k2.start()
        k3 = QMovie("../_qt_ui/poke/k/k3.gif")
        self.poke3.label_pokemon3.setMovie(k3)
        k3.start()

    def eee(self):
        e1 = QMovie("../_qt_ui/poke/e/e1.gif")
        self.poke3.label_pokemon1.setMovie(e1)
        e1.start()
        e2 = QMovie("../_qt_ui/poke/e/e2.gif")
        self.poke3.label_pokemon2.setMovie(e2)
        e2.start()
        e3 = QMovie("../_qt_ui/poke/e/e3.gif")
        self.poke3.label_pokemon3.setMovie(e3)
        e3.start()
########################################################################################################################
class skill_image:
    def p(self):
        self.poke3.label_skill1.setStyleSheet(
            'image:url(../_qt_ui/poke/p/백만볼트.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill2.setStyleSheet(
            'image:url(../_qt_ui/poke/p/전기쇼크.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill3.setStyleSheet(
            'image:url(../_qt_ui/poke/p/번개.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill4.setStyleSheet(
            'image:url(../_qt_ui/poke/p/볼트태클.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill5.setStyleSheet(
            'image:url(../_qt_ui/poke/p/엘렉트릭네트.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
    def f(self):
        self.poke3.label_skill1.setStyleSheet(
            'image:url(../_qt_ui/poke/f/불꽃펀치.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill2.setStyleSheet(
            'image:url(../_qt_ui/poke/f/화염방사.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill3.setStyleSheet(
            'image:url(../_qt_ui/poke/f/회오리불꽃.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill4.setStyleSheet(
            'image:url(../_qt_ui/poke/f/불대문자.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill5.setStyleSheet(
            'image:url(../_qt_ui/poke/f/지구던지기.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
    def k(self):
        self.poke3.label_skill1.setStyleSheet(
            'image:url(../_qt_ui/poke/k/물대포.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill2.setStyleSheet(
            'image:url(../_qt_ui/poke/k/거품.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill3.setStyleSheet(
            'image:url(../_qt_ui/poke/k/파도타기.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill4.setStyleSheet(
            'image:url(../_qt_ui/poke/k/열탕.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
        self.poke3.label_skill5.setStyleSheet(
            'image:url(../_qt_ui/poke/k/바다회오리.png); color: rgb(53, 100, 173); background-color: rgb(0, 0, 0);')
    def e(self):
        self.poke3.label_skill1.setStyleSheet(
            'image:url(../_qt_ui/poke/e/잎날가르기.png); color: rgb(53, 100, 173); background-color: rgb(255, 203, 5);')
        self.poke3.label_skill2.setStyleSheet(
            'image:url(../_qt_ui/poke/e/씨폭탄.png); color: rgb(53, 100, 173); background-color: rgb(255, 203, 5);')
        self.poke3.label_skill3.setStyleSheet(
            'image:url(../_qt_ui/poke/e/기가드레인.png); color: rgb(53, 100, 173); background-color: rgb(255, 203, 5);')
        self.poke3.label_skill4.setStyleSheet(
            'image:url(../_qt_ui/poke/e/솔라빔.png); color: rgb(53, 100, 173); background-color: rgb(255, 203, 5);')
        self.poke3.label_skill5.setStyleSheet(
            'image:url(../_qt_ui/poke/e/오물폭탄.png); color: rgb(53, 100, 173); background-color: rgb(255, 203, 5);')
########################################################################################################################
class messagebox(gif, skill_image):
    def __init__(self):
        gif.__init__(self)
        skill_image.__init__(self)

    def end1(self):
        ### 피카츄 ##########################################################################
        if self.label_my.text() == variable_value.my_level[0][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[0][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
            gif.ppp(self)
            skill_image.p(self)
        elif self.label_my.text() == variable_value.my_level[0][1]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[0][1])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
            gif.ppp(self)
            skill_image.p(self)
        elif self.label_my.text() == variable_value.my_level[0][2]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[0][2])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
            gif.ppp(self)
            skill_image.p(self)
        elif self.label_my.text() == variable_value.my_level[0][3]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[0][3])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
            gif.ppp(self)
            skill_image.p(self)

        ### 파이리 ##########################################################################
        elif self.label_my.text() == variable_value.my_level[1][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[1][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm1.png);')
            gif.fff(self)
            skill_image.f(self)
        elif self.label_my.text() == variable_value.my_level[1][1]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[1][1])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm2.png);')
            gif.fff(self)
            skill_image.f(self)
        elif self.label_my.text() == variable_value.my_level[1][2]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[1][2])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm2.png);')
            gif.fff(self)
            skill_image.f(self)
        elif self.label_my.text() == variable_value.my_level[1][3]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[1][3])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm3.png);')
            gif.fff(self)
            skill_image.f(self)

        ### 꼬부기 ##########################################################################
        elif self.label_my.text() == variable_value.my_level[2][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[2][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km1.png);')
            gif.kkk(self)
            skill_image.k(self)
        elif self.label_my.text() == variable_value.my_level[2][1]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[2][1])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km2.png);')
            gif.kkk(self)
            skill_image.k(self)
        elif self.label_my.text() == variable_value.my_level[2][2]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[2][2])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km2.png);')
            gif.kkk(self)
            skill_image.k(self)
        elif self.label_my.text() == variable_value.my_level[2][3]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[2][3])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km3.png);')
            gif.kkk(self)
            skill_image.k(self)

        ### 이상해씨 #########################################################################
        elif self.label_my.text() == variable_value.my_level[3][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[3][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em1.png);')
            gif.eee(self)
            skill_image.e(self)
        elif self.label_my.text() == variable_value.my_level[3][1]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[3][1])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em2.png);')
            gif.eee(self)
            skill_image.e(self)
        elif self.label_my.text() == variable_value.my_level[3][2]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[3][2])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em2.png);')
            gif.eee(self)
            skill_image.e(self)
        elif self.label_my.text() == variable_value.my_level[3][3]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[3][3])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em3.png);')
            gif.eee(self)
            skill_image.e(self)

    def end2(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setWindowTitle("INFO BY STARBUCKS")
        msgBox.setText("경험치 {} 획득".format(variable_value.ex))
        msgBox.setInformativeText("메소 {} 획득".format(variable_value.gm))
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        variable_value.game_money += variable_value.gm
        num = re.findall(r'\d+', self.label_my.text())
        num = num[0]
        if int(num) == 1:
            variable_value.level1_ex += variable_value.ex
        elif int(num) == 2:
            variable_value.level2_ex += variable_value.ex
        elif int(num) == 3:
            variable_value.level3_ex += variable_value.ex
        elif int(num) == 4:
            variable_value.level4_ex += variable_value.ex
        a = msgBox.exec_()
        if a == QMessageBox.Ok:
            self.poke3 = poke3()
            if variable_value.page3_level[0] == variable_value.my_level[0][0]:
                gif.ppp(self)
                skill_image.p(self)
                if variable_value.level1_ex < 60:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level1_ex) + " / " + str(60))
                    self.poke3.label_pokemon_name.setText(self.label_my.text())
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
                elif variable_value.level2_ex < 90:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level2_ex) + " / " + str(90))  # 240
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[0][1])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
                elif variable_value.level3_ex < 120:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level3_ex) + " / " + str(120))  # 792
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[0][2])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
                elif variable_value.level4_ex < 150:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level4_ex) + " / " + str(150))  # 3564
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[0][3])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
                elif variable_value.level4_ex > 250:
                    pass
            elif variable_value.page3_level[0] == variable_value.my_level[1][0]:
                gif.fff(self)
                skill_image.f(self)
                if variable_value.level1_ex < 60:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level1_ex) + " / " + str(60))
                    self.poke3.label_pokemon_name.setText(self.label_my.text())
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm1.png);')
                elif variable_value.level2_ex < 90:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level2_ex) + " / " + str(90)) # 240
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[1][1])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm2.png);')
                elif variable_value.level3_ex < 120:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level3_ex) + " / " + str(120)) # 792
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[1][2])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm2.png);')
                elif variable_value.level4_ex < 150:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level4_ex) + " / " + str(150)) # 3564
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[1][3])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm3.png);')
                elif variable_value.level4_ex > 250:
                    pass
            elif variable_value.page3_level[0] == variable_value.my_level[2][0]:
                gif.kkk(self)
                skill_image.k(self)
                if variable_value.level1_ex < 60:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level1_ex) + " / " + str(60))
                    self.poke3.label_pokemon_name.setText(self.label_my.text())
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km1.png);')
                elif variable_value.level2_ex < 90:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level2_ex) + " / " + str(90)) # 240
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[2][1])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km2.png);')
                elif variable_value.level3_ex < 120:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level3_ex) + " / " + str(120)) # 792
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[2][2])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km2.png);')
                elif variable_value.level4_ex < 150:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level4_ex) + " / " + str(150)) # 3564
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[2][3])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km3.png);')
                elif variable_value.level4_ex > 250:
                    pass
            elif variable_value.page3_level[0] == variable_value.my_level[3][0]:
                gif.eee(self)
                skill_image.e(self)
                if variable_value.level1_ex < 60:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level1_ex) + " / " + str(60))
                    self.poke3.label_pokemon_name.setText(self.label_my.text())
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em1.png);')
                elif variable_value.level2_ex < 90:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level2_ex) + " / " + str(90)) # 240
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[3][1])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em2.png);')
                elif variable_value.level3_ex < 120:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level3_ex) + " / " + str(120)) # 792
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[3][2])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em2.png);')
                elif variable_value.level4_ex < 150:
                    self.poke3.label_ex.setText("EX " + str(variable_value.level4_ex) + " / " + str(150)) # 3564
                    self.poke3.label_pokemon_name.setText(variable_value.my_level[3][3])
                    self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em3.png);')
                elif variable_value.level4_ex > 250:
                    pass
            self.poke3.show()
            self.close()
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
### CLASS 4 ############################################################################################################
class poke4(QMainWindow, messagebox):
    def __init__(self):
        QMainWindow.__init__(self)
        messagebox.__init__(self)
        loadUi(UI4, self)

        self.pushButton_hp.setStyleSheet('QPushButton{image:url(../_qt_ui/icon/icon_hp48.png); color: rgb(255, 0, 0); background-color: rgb(255, 203, 5); border-radius: 10px; font: 12pt "휴먼매직체";} QPushButton:hover{background-color: rgb(255, 255, 127);}')
        self.pushButton_mp.setStyleSheet('QPushButton{image:url(../_qt_ui/icon/icon_mp48.png); color: rgb(0, 85, 255); background-color: rgb(255, 203, 5); border-radius: 10px; font: 12pt "휴먼매직체";} QPushButton:hover{background-color: rgb(255, 255, 127);}')
        self.pushButton_hp.setText("\n\n\n0 개")
        self.pushButton_mp.setText("\n\n\n0 개")

        # 나의 HP, MP
        self.progressBar_hp.setValue(variable_value.my_hp)
        self.progressBar_mp.setValue(variable_value.my_mp)
        # 상대 HP, MP
        self.progressBar_op_hp.setValue(100)
        self.progressBar_op_mp.setValue(100)

        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_skill1.clicked.connect(lambda state, button = self.pushButton_skill1, damaged1 = 10, damaged2 = 25, damaged3 = 35, damaged4 = 50, damaged5 = 100,\
                                                   skill2 = 30, skill3 = 40, skill4 = 80, skill5 = 150\
                                                   : self.skill(state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5))
        self.pushButton_skill2.clicked.connect(lambda state, button = self.pushButton_skill2, damaged1 = 10, damaged2 = 25, damaged3 = 35, damaged4 = 50, damaged5 = 100,\
                                                   skill2 = 30, skill3 = 40, skill4 = 80, skill5 = 150\
                                                   : self.skill(state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5))
        self.pushButton_skill3.clicked.connect(lambda state, button = self.pushButton_skill3, damaged1 = 10, damaged2 = 25, damaged3 = 35, damaged4 = 50, damaged5 = 100,\
                                                   skill2 = 30, skill3 = 40, skill4 = 80, skill5 = 150\
                                                   : self.skill(state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5))
        self.pushButton_skill4.clicked.connect(lambda state, button = self.pushButton_skill4, damaged1 = 10, damaged2 = 25, damaged3 = 35, damaged4 = 50, damaged5 = 100,\
                                                   skill2 = 30, skill3 = 40, skill4 = 80, skill5 = 150\
                                                   : self.skill(state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5))
        self.pushButton_skill5.clicked.connect(lambda state, button = self.pushButton_skill5, damaged1 = 10, damaged2 = 25, damaged3 = 35, damaged4 = 50, damaged5 = 100,\
                                                   skill2 = 30, skill3 = 40, skill4 = 80, skill5 = 150\
                                                   : self.skill(state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5))
        self.pushButton_hp.clicked.connect(self.potion)
        self.pushButton_mp.clicked.connect(self.potion)


    def potion(self):
        self.listWidget.addItem("아직 사용 할 수 없는 기능입니다...")
    ### 전투 중 종료 시 메세지 ##########################################################
    def back(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setWindowTitle("Notification")
        msgBox.setText("전투 중 게임을 종료 시\n경험치와 메소를 획득 하실 수 없습니다.")
        msgBox.setInformativeText("그래도 종료하시겠습니까?")
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msgBox.setDefaultButton(QMessageBox.No)
        a = msgBox.exec_()
        if a == QMessageBox.Yes:
            self.poke3 = poke3()
            messagebox.end1(self)
            self.poke3.show()
            self.close()

    def skill(self, state, button, damaged1, damaged2, damaged3, damaged4, damaged5, skill2, skill3, skill4, skill5):
        if button == self.pushButton_skill1:
            self.listWidget.addItem("데미지 {} 공격".format(damaged1))
            # self.label_opdamaged.setText("hi")
            a = self.progressBar_op_hp.value() - damaged1
            self.progressBar_op_hp.setValue(a)
            ###
            tt = self.progressBar_hp.value() - variable_value.ta
            self.progressBar_hp.setValue(tt)
            self.listWidget.addItem("적으로부터 데이지 {} 입었습니다.".format(variable_value.ta))
            if a <= 0:
                self.progressBar_op_hp.setValue(0)
                messagebox.end2(self)

        elif button == self.pushButton_skill2:
            self.listWidget.addItem("데미지 {} 공격".format(damaged2))
            b = self.progressBar_op_hp.value() - damaged2
            self.progressBar_op_hp.setValue(b)
            b2 = self.progressBar_mp.value() - skill2
            self.progressBar_mp.setValue(b2)
            ###
            tt = self.progressBar_hp.value() - variable_value.ta
            self.progressBar_hp.setValue(tt)
            self.listWidget.addItem("적으로부터 데이지 {} 입었습니다.".format(variable_value.ta))
            if b <= 0:
                self.progressBar_op_hp.setValue(0)
                messagebox.end2(self)
            if b2 <= 0:
                self.progressBar_mp.setValue(0)

        elif button == self.pushButton_skill3:
            self.listWidget.addItem("데미지 {} 공격".format(damaged3))
            c = self.progressBar_op_hp.value() - damaged3
            self.progressBar_op_hp.setValue(c)
            c2 = self.progressBar_mp.value() - skill3
            self.progressBar_mp.setValue(c2)
            ###
            tt = self.progressBar_hp.value() - variable_value.ta
            self.progressBar_hp.setValue(tt)
            self.listWidget.addItem("적으로부터 데이지 {} 입었습니다.".format(variable_value.ta))
            if c <= 0:
                self.progressBar_op_hp.setValue(0)
                messagebox.end2(self)
            if c2 <= 0:
                self.progressBar_mp.setValue(0)

        elif button == self.pushButton_skill4:
            self.listWidget.addItem("데미지 {} 공격".format(damaged4))
            d = self.progressBar_op_hp.value() - damaged4
            self.progressBar_op_hp.setValue(d)
            d2 = self.progressBar_mp.value() - skill4
            self.progressBar_mp.setValue(d2)
            ###
            tt = self.progressBar_hp.value() - variable_value.ta
            self.progressBar_hp.setValue(tt)
            self.listWidget.addItem("적으로부터 데이지 {} 입었습니다.".format(variable_value.ta))
            if d <= 0:
                self.progressBar_op_hp.setValue(0)
                messagebox.end2(self)
            if d2 <= 0:
                self.progressBar_mp.setValue(0)

        elif button == self.pushButton_skill5:
            self.listWidget.addItem("데미지 [ {} ] 입혔습니다.".format(damaged5))
            e = self.progressBar_op_hp.value() - damaged5
            self.progressBar_op_hp.setValue(e)
            e2 = self.progressBar_mp.value() - skill5
            self.progressBar_mp.setValue(e2)
            ###
            tt = self.progressBar_hp.value() - variable_value.ta
            self.progressBar_hp.setValue(tt)
            self.listWidget.addItem("적으로부터 데이지 {} 입었습니다.".format(variable_value.ta))
            if e <= 0:
                self.progressBar_op_hp.setValue(0)
                messagebox.end2(self)
            if e2 <= 0:
                self.progressBar_mp.setValue(0)

### CLASS 3 ############################################################################################################
class poke3(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(UI3, self)

        self.label_player_name.setText(variable_value.my_name[0])
        self.label_game_money.setText(str(variable_value.game_money) + " 메소")
        self.label_player_image.setStyleSheet('image:url(../_qt_ui/poke/jiu.png);')

        ### MY_HP #######################################################
        self.progressBar_hp.setRange(variable_value.minimum_hpmp, variable_value.my_hp)
        self.progressBar_hp.setValue(variable_value.my_hp)
        ### MY_MP #######################################################
        self.progressBar_mp.setRange(variable_value.minimum_hpmp, variable_value.my_mp)
        self.progressBar_mp.setValue(variable_value.my_mp)
        ### MY_EX #######################################################
        # self.progressBar_ex.setRange(variable_value.minimum_hpmp, variable_value.maximum_ex)
        # self.progressBar_ex.setValue(variable_value.experience_value)
        self.label_hp.setStyleSheet('image:url(../_qt_ui/icon/icon_hp48.png); color: rgb(255, 0, 0); background-color: rgb(255, 203, 5); font: 12pt "휴먼매직체";')
        self.label_mp.setStyleSheet('image:url(../_qt_ui/icon/icon_mp48.png); color: rgb(0, 85, 255); background-color: rgb(255, 203, 5); font: 12pt "휴먼매직체";')
        self.label_hp.setText("\n\n\n0 개")
        self.label_mp.setText("\n\n\n0 개")

        self.pushButton_fight.clicked.connect(self.fight)
        self.pushButton_book.clicked.connect(self.book)
        self.pushButton_buypotion.clicked.connect(self.buypotion)

    ### SIGNAL ##########################################################
    def fight(self):
        self.poke4 = poke4()
        self.poke4.label_my.setText(self.label_pokemon_name.text())
        # print(self.label_pokemon_name.text())
        # print(self.poke4.label_my.text())

        ### 피카츄 #######################################################
        p = self.label_pokemon_name.text()
        if p == variable_value.my_level[0][0] or p == variable_value.my_level[0][1] or p == variable_value.my_level[0][2] or p == variable_value.my_level[0][3]:
            m = QMovie("../_qt_ui/poke/m/p3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        ### 파이리 #######################################################
        elif self.label_pokemon_name.text() == variable_value.my_level[1][0]:
            m = QMovie("../_qt_ui/poke/m/f1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[1][1] or self.label_pokemon_name.text() == variable_value.my_level[1][2]:
            m = QMovie("../_qt_ui/poke/m/f2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[1][3]:
            m = QMovie("../_qt_ui/poke/m/f3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        ### 꼬부기 #######################################################
        elif self.label_pokemon_name.text() == variable_value.my_level[2][0]:
            m = QMovie("../_qt_ui/poke/m/k1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[2][1] or self.label_pokemon_name.text() == variable_value.my_level[2][2]:
            m = QMovie("../_qt_ui/poke/m/k2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[2][3]:
            m = QMovie("../_qt_ui/poke/m/k3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        ### 이상해씨 #####################################################
        elif self.label_pokemon_name.text() == variable_value.my_level[3][0]:
            m = QMovie("../_qt_ui/poke/m/e1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[3][1] or self.label_pokemon_name.text() == variable_value.my_level[3][2]:
            m = QMovie("../_qt_ui/poke/m/e2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == variable_value.my_level[3][3]:
            m = QMovie("../_qt_ui/poke/m/e3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()

        ### 포켓몬 스킬 ##################################################
        onlystring = re.compile("[가-힣]+").findall(self.label_pokemon_name.text())
        onlystring = onlystring[0]
        if onlystring == "피카츄":
            self.poke4.pushButton_skill1.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/p/백만볼트.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 203, 5);}')
            self.poke4.pushButton_skill2.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/p/전기쇼크.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 203, 5);}')
            self.poke4.pushButton_skill3.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/p/번개.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 203, 5);}')
            self.poke4.pushButton_skill4.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/p/볼트태클.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 203, 5);}')
            self.poke4.pushButton_skill5.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/p/엘렉트릭네트.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 203, 5);}')
        elif onlystring == "파이리" or onlystring == "리자드" or onlystring == "리자몽":
            self.poke4.pushButton_skill1.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/f/불꽃펀치.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 85, 0);}')
            self.poke4.pushButton_skill2.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/f/화염방사.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 85, 0);}')
            self.poke4.pushButton_skill3.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/f/회오리불꽃.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 85, 0);}')
            self.poke4.pushButton_skill4.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/f/불대문자.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 85, 0);}')
            self.poke4.pushButton_skill5.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/f/지구던지기.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(255, 85, 0);}')
        elif onlystring == "꼬부기" or onlystring == "어니부기" or onlystring == "거북왕":
            self.poke4.pushButton_skill1.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/k/물대포.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(0, 170, 255);}')
            self.poke4.pushButton_skill2.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/k/거품.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(0, 170, 255);}')
            self.poke4.pushButton_skill3.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/k/파도타기.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(0, 170, 255);}')
            self.poke4.pushButton_skill4.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/k/열탕.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(0, 170, 255);}')
            self.poke4.pushButton_skill5.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/k/바다회오리.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(0, 170, 255);}')
        elif onlystring == "이상해씨" or onlystring == "이상해풀" or onlystring == "이상해꽃":
            self.poke4.pushButton_skill1.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/e/잎날가르기.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(85, 255, 0);}')
            self.poke4.pushButton_skill2.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/e/씨폭탄.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(85, 255, 0);}')
            self.poke4.pushButton_skill3.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/e/기가드레인.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(85, 255, 0);}')
            self.poke4.pushButton_skill4.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/e/솔라빔.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(85, 255, 0);}')
            self.poke4.pushButton_skill5.setStyleSheet('QPushButton{image:url(../_qt_ui/poke/e/오물폭탄.png); background-color: rgb(0, 0, 0); border-radius: 10px;} QPushButton:hover{background-color: rgb(170, 85, 255);}')

        ### 상대 몬스터 ##################################################
        ### 나의 레벨에 맞춰 상대몬스터 등장
        ### 여기에 4, 5레벨 때 스킬 풀림 ###################################
        level_1 = randint(0, 7)
        level_2 = randint(3, 17)
        level_3 = randint(8, 27)
        level_4 = randint(18, 37)
        num = re.sub(r'[^0-9]', '', self.label_pokemon_name.text())
        if int(num) == 1:
            ops = oppsing.op_list[level_1]
            op = QMovie(ops)
            self.poke4.label_oppokemon.setMovie(op)
            op.start()
            if ops == '../_qt_ui/poke/op/1/op1.gif':
                self.poke4.label_op.setText("Lv. 1 나옹")
            elif ops == '../_qt_ui/poke/op/1/op2.gif':
                self.poke4.label_op.setText("Lv. 1 이브이")
            elif ops == '../_qt_ui/poke/op/1/op3.gif':
                self.poke4.label_op.setText("Lv. 1 푸린")
            elif ops == '../_qt_ui/poke/op/2/op1.gif':
                self.poke4.label_op.setText("Lv. 2 내루미")
            elif ops == '../_qt_ui/poke/op/2/op2.gif':
                self.poke4.label_op.setText("Lv. 2 또도가스")
            elif ops == '../_qt_ui/poke/op/2/op3.gif':
                self.poke4.label_op.setText("Lv. 2 마자용")
            elif ops == '../_qt_ui/poke/op/2/op4.gif':
                self.poke4.label_op.setText("Lv. 2 아보크")
            elif ops == '../_qt_ui/poke/op/2/op5.gif':
                self.poke4.label_op.setText("Lv. 2 우츠보트")
            self.poke4.pushButton_skill4.setEnabled(False)
            self.poke4.pushButton_skill5.setEnabled(False)
        elif int(num) == 2:
            ops = oppsing.op_list[level_2]
            op = QMovie(ops)
            self.poke4.label_oppokemon.setMovie(op)
            op.start()
            if ops == '../_qt_ui/poke/op/2/op1.gif':
                self.poke4.label_op.setText("Lv. 2 내루미")
            elif ops == '../_qt_ui/poke/op/2/op2.gif':
                self.poke4.label_op.setText("Lv. 2 또도가스")
            elif ops == '../_qt_ui/poke/op/2/op3.gif':
                self.poke4.label_op.setText("Lv. 2 마자용")
            elif ops == '../_qt_ui/poke/op/2/op4.gif':
                self.poke4.label_op.setText("Lv. 2 아보크")
            elif ops == '../_qt_ui/poke/op/2/op5.gif':
                self.poke4.label_op.setText("Lv. 2 우츠보트")
            elif ops == '../_qt_ui/poke/op/3/op1.gif':
                self.poke4.label_op.setText("Lv. 3 괴력몬")
            elif ops == '../_qt_ui/poke/op/3/op2.gif':
                self.poke4.label_op.setText("Lv. 3 닥트리오")
            elif ops == '../_qt_ui/poke/op/3/op3.gif':
                self.poke4.label_op.setText("Lv. 3 마그마")
            elif ops == '../_qt_ui/poke/op/3/op4.gif':
                self.poke4.label_op.setText("Lv. 3 잠만보")
            elif ops == '../_qt_ui/poke/op/3/op5.gif':
                self.poke4.label_op.setText("Lv. 3 전룡")
            elif ops == '../_qt_ui/poke/op/3/op6.gif':
                self.poke4.label_op.setText("Lv. 3 질뻐기")
            elif ops == '../_qt_ui/poke/op/3/op7.gif':
                self.poke4.label_op.setText("Lv. 3 켄타로스")
            elif ops == '../_qt_ui/poke/op/3/op8.gif':
                self.poke4.label_op.setText("Lv. 3 팬텀")
            elif ops == '../_qt_ui/poke/op/3/op9.gif':
                self.poke4.label_op.setText("Lv. 3 헤라크로스")
            elif ops == '../_qt_ui/poke/op/3/op10.gif':
                self.poke4.label_op.setText("Lv. 3 후딘")
            self.poke4.pushButton_skill4.setEnabled(True)
            self.poke4.pushButton_skill5.setEnabled(False)
        elif int(num) == 3:
            ops = oppsing.op_list[level_3]
            op = QMovie(ops)
            self.poke4.label_oppokemon.setMovie(op)
            op.start()
            if ops == '../_qt_ui/poke/op/3/op1.gif':
                self.poke4.label_op.setText("Lv. 3 괴력몬")
            elif ops == '../_qt_ui/poke/op/3/op2.gif':
                self.poke4.label_op.setText("Lv. 3 닥트리오")
            elif ops == '../_qt_ui/poke/op/3/op3.gif':
                self.poke4.label_op.setText("Lv. 3 마그마")
            elif ops == '../_qt_ui/poke/op/3/op4.gif':
                self.poke4.label_op.setText("Lv. 3 잠만보")
            elif ops == '../_qt_ui/poke/op/3/op5.gif':
                self.poke4.label_op.setText("Lv. 3 전룡")
            elif ops == '../_qt_ui/poke/op/3/op6.gif':
                self.poke4.label_op.setText("Lv. 3 질뻐기")
            elif ops == '../_qt_ui/poke/op/3/op7.gif':
                self.poke4.label_op.setText("Lv. 3 켄타로스")
            elif ops == '../_qt_ui/poke/op/3/op8.gif':
                self.poke4.label_op.setText("Lv. 3 팬텀")
            elif ops == '../_qt_ui/poke/op/3/op9.gif':
                self.poke4.label_op.setText("Lv. 3 헤라크로스")
            elif ops == '../_qt_ui/poke/op/3/op10.gif':
                self.poke4.label_op.setText("Lv. 3 후딘")
            elif ops == '../_qt_ui/poke/op/4/op1.gif':
                self.poke4.label_op.setText("Lv. 4 개굴닌자")
            elif ops == '../_qt_ui/poke/op/4/op2.gif':
                self.poke4.label_op.setText("Lv. 4 갸라도스")
            elif ops == '../_qt_ui/poke/op/4/op3.gif':
                self.poke4.label_op.setText("Lv. 4 라프라스")
            elif ops == '../_qt_ui/poke/op/4/op4.gif':
                self.poke4.label_op.setText("Lv. 4 마기라스")
            elif ops == '../_qt_ui/poke/op/4/op5.gif':
                self.poke4.label_op.setText("Lv. 4 망나뇽")
            elif ops == '../_qt_ui/poke/op/4/op6.gif':
                self.poke4.label_op.setText("Lv. 4 메타그로스")
            elif ops == '../_qt_ui/poke/op/4/op7.gif':
                self.poke4.label_op.setText("Lv. 4 보만다")
            elif ops == '../_qt_ui/poke/op/4/op8.gif':
                self.poke4.label_op.setText("Lv. 4 삼삼드래")
            elif ops == '../_qt_ui/poke/op/4/op9.gif':
                self.poke4.label_op.setText("Lv. 4 한카리아스")
            elif ops == '../_qt_ui/poke/op/4/op10.gif':
                self.poke4.label_op.setText("Lv. 4 해피너스")
            self.poke4.pushButton_skill4.setEnabled(True)
            self.poke4.pushButton_skill5.setEnabled(False)
        elif int(num) == 4:
            ops = oppsing.op_list[level_4]
            op = QMovie(ops)
            self.poke4.label_oppokemon.setMovie(op)
            op.start()
            if ops == '../_qt_ui/poke/op/4/op1.gif':
                self.poke4.label_op.setText("Lv. 4 개굴닌자")
            elif ops == '../_qt_ui/poke/op/4/op2.gif':
                self.poke4.label_op.setText("Lv. 4 갸라도스")
            elif ops == '../_qt_ui/poke/op/4/op3.gif':
                self.poke4.label_op.setText("Lv. 4 라프라스")
            elif ops == '../_qt_ui/poke/op/4/op4.gif':
                self.poke4.label_op.setText("Lv. 4 마기라스")
            elif ops == '../_qt_ui/poke/op/4/op5.gif':
                self.poke4.label_op.setText("Lv. 4 망나뇽")
            elif ops == '../_qt_ui/poke/op/4/op6.gif':
                self.poke4.label_op.setText("Lv. 4 메타그로스")
            elif ops == '../_qt_ui/poke/op/4/op7.gif':
                self.poke4.label_op.setText("Lv. 4 보만다")
            elif ops == '../_qt_ui/poke/op/4/op8.gif':
                self.poke4.label_op.setText("Lv. 4 삼삼드래")
            elif ops == '../_qt_ui/poke/op/4/op9.gif':
                self.poke4.label_op.setText("Lv. 4 한카리아스")
            elif ops == '../_qt_ui/poke/op/4/op10.gif':
                self.poke4.label_op.setText("Lv. 4 해피너스")
            elif ops == '../_qt_ui/poke/op/5/op1.gif':
                self.poke4.label_op.setText("Lv. 5 루기아")
            elif ops == '../_qt_ui/poke/op/5/op2.gif':
                self.poke4.label_op.setText("Lv. 5 메가니움")
            elif ops == '../_qt_ui/poke/op/5/op3.gif':
                self.poke4.label_op.setText("Lv. 5 뮤")
            elif ops == '../_qt_ui/poke/op/5/op4.gif':
                self.poke4.label_op.setText("Lv. 5 뮤츠")
            elif ops == '../_qt_ui/poke/op/5/op5.gif':
                self.poke4.label_op.setText("Lv. 5 스이쿤")
            elif ops == '../_qt_ui/poke/op/5/op6.gif':
                self.poke4.label_op.setText("Lv. 5 썬더")
            elif ops == '../_qt_ui/poke/op/5/op7.gif':
                self.poke4.label_op.setText("Lv. 5 칠색조")
            elif ops == '../_qt_ui/poke/op/5/op8.gif':
                self.poke4.label_op.setText("Lv. 5 파이어")
            elif ops == '../_qt_ui/poke/op/5/op9.gif':
                self.poke4.label_op.setText("Lv. 5 파치리스")
            elif ops == '../_qt_ui/poke/op/5/op10.gif':
                self.poke4.label_op.setText("Lv. 5 프리저")
            self.poke4.pushButton_skill4.setEnabled(True)
            self.poke4.pushButton_skill5.setEnabled(True)
        self.poke4.show()
        self.close()


    def book(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setWindowTitle("Notification")
        msgBox.setText("준비 중...")
        msgBox.setInformativeText("T-T...")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec_()

    def buypotion(self):
        msgBox = QMessageBox()
        msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_pokemon96.png"))
        msgBox.setWindowTitle("Notification")
        msgBox.setText("준비 중...")
        msgBox.setInformativeText("T-T...")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setDefaultButton(QMessageBox.Ok)
        msgBox.exec_()

########################################################################################################################
class poke_potion(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(UI_potion, self)

### CLASS 2 ############################################################################################################
class poke2(QDialog, gif, skill_image):
    def __init__(self):
        QDialog.__init__(self)
        gif.__init__(self)
        skill_image.__init__(self)
        loadUi(UI2, self)

        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_back.clicked.connect(self.back)

    ### SIGNAL ##################################################
    def next(self):
        variable_value.my_name.append(self.lineEdit.text())
        self.poke3 = poke3()
        self.poke3.label_ex.setText("EX " + str(variable_value.level1_ex) + " / " + str(100))
        if self.label_pokemon_name.text() == variable_value.my_level[0][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[0][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/pm1.png);')
            gif.ppp(self)
            skill_image.p(self)
        elif self.label_pokemon_name.text() == variable_value.my_level[1][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[1][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/fm1.png);')
            gif.fff(self)
            skill_image.f(self)
        elif self.label_pokemon_name.text() == variable_value.my_level[2][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[2][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/km1.png);')
            gif.kkk(self)
            skill_image.k(self)
        elif self.label_pokemon_name.text() == variable_value.my_level[3][0]:
            self.poke3.label_pokemon_name.setText(variable_value.my_level[3][0])
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/em1.png);')
            gif.eee(self)
            skill_image.e(self)
        self.poke3.show()
        pokemon.close()
        self.close()

    ### SIGNAL ##################################################
    def back(self):
        variable_value.page3_level.clear()
        pokemon.show()
        self.close()

    ### SIGNAL ##################################################
    def modal(self):
        self.setModal(True)
        self.show()

### CLASS ##############################################################################################################
class poke1(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        loadUi(UI1, self)

        ### 피카츄 ###############################################
        p = (QMovie("../_qt_ui/poke/p/p1.gif"))
        self.label_ppp.setMovie(p)
        p.start()
        ### 파이리 ###############################################
        f = (QMovie("../_qt_ui/poke/f/f1.gif"))
        self.label_fff.setMovie(f)
        f.start()
        ### 꼬부기 ###############################################
        k = (QMovie("../_qt_ui/poke/k/k1.gif"))
        self.label_kkk.setMovie(k)
        k.start()
        ### 이상해씨 #############################################
        e = (QMovie("../_qt_ui/poke/e/e1.gif"))
        self.label_eee.setMovie(e)
        e.start()

        self.pushButton_ppp.clicked.connect(lambda state, button = self.pushButton_ppp, pokemon = variable_value.my_level[0][0] : self.profile(state, button, pokemon))
        self.pushButton_fff.clicked.connect(lambda state, button = self.pushButton_fff, pokemon = variable_value.my_level[1][0] : self.profile(state, button, pokemon))
        self.pushButton_kkk.clicked.connect(lambda state, button = self.pushButton_kkk, pokemon = variable_value.my_level[2][0] : self.profile(state, button, pokemon))
        self.pushButton_eee.clicked.connect(lambda state, button = self.pushButton_eee, pokemon = variable_value.my_level[3][0] : self.profile(state, button, pokemon))

    ### SIGNAL #########################################################################################################
    def profile(self, state, button, pokemon):
        self.poke2 = poke2()
        self.poke2.label_pokemon_name.setText(pokemon)
        variable_value.page3_level.append(pokemon)
        print(variable_value.page3_level[0])
        self.poke2.modal()

########################################################################################################################
IlovePython = QApplication(sys.argv)
pokemon = poke1()
pokemon.show()
IlovePython.exec()