import random
import time
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5 import QtWidgets, QtGui, QtCore

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.loadUi = uic.loadUi("start.ui",self)
        self.new_.clicked.connect(self.go_new)
        self.load_.clicked.connect(self.go_load)
        self.quit_.clicked.connect(self.go_quit)

    def go_new(self):
        Pok_select().show()
        self.close()

    def go_load(self):
        pass

    def go_quit(self):
        self.close()


class Pok_select(QWidget):
    user = []
    GP = []
    def __init__(self):
        super().__init__()
        self.loadUi = uic.loadUi("pok_select.ui",self)
        self.sel_pok.hide()
        self.lineEdit.setText("너는 누구니?")
        self.textEdit.hide()
        self.ok.clicked.connect(self.ok_name)
        self.pikachu.clicked.connect(self.get_pikachu)
        self.piry.clicked.connect(self.get_piry)
        self.ggobook.clicked.connect(self.get_ggobook)
        self.isanghae.clicked.connect(self.get_isanghae)


    def ok_name(self):
        self.user.append(self.input_name.text())
        self.name_frame.hide()
        self.sel_pok.show()
        self.textEdit.show()
        self.lineEdit.setText("이야- 오래 기다리게 했다!\n포켓몬스터의 세계에 잘왔단다!\n나의 이름은 오박사\n"
                              "모두로부터는 포켓몬박사라고 존경받고 있단다.\n포켓몬스터.........포켓몬\n"
                              "이 세계에는 포켓몬스터라고 불려지는 생명체들이\n도처에 살고있다! [마릴~]\n"
                              "사람은 포켓몬들과 정답게 지내거나 함께 싸우거나........\n"
                              """서로 도와가며 살아가고 있단다
하지만 우리들은 포켓몬 전부를 알고 있지는 못하다
포켓몬의 비밀은 아직도 잔뜩 있다!""")

    def get_pikachu(self):
        self.GP.append("피카츄")
        Game_Start().show()
        self.close()
    def get_piry(self):
        self.GP.append("파이리")
        Game_Start().show()
        self.close()
    def get_ggobook(self):
        self.GP.append("꼬부기")
        Game_Start().show()
        self.close()
    def get_isanghae(self):
        self.GP.append("이상해씨")
        Game_Start().show()
        self.close()

Lvl = 1
Bhp = 500
potion = 5
MPHp = 500
EPHp = 500
EPHp1 = EPHp
Mid = 100
Mad = 200
MPBa = random.randint(Mid, Mad)
EPBa = random.randint(int(Mid * 9 / 10), int(Mad * 9 / 10))
class Game_Start(QWidget):
    user = Pok_select.user
    GP = Pok_select.GP
    def __init__(self):
        global Lvl, Bhp, potion, MPHp, EPHp, Mid, Mad, EPBa, MPBa, EPHp1
        super().__init__()
        self.loadUi = uic.loadUi("game_start.ui",self)
        self.pok_name.setText(f"{self.GP[0]}\tLv.{str(Lvl)}")
        self.pok_info.setText(f"체력/현재체력 : {Bhp}/{MPHp}\n공격력 : {Mid}~{Mad}\n포션개수 : {potion}")
        self.adventure.clicked.connect(self.go_adv)
        self.pok_center.clicked.connect(self.go_pok_c)
        self.quit_.clicked.connect(self.go_quit)
        if self.GP[0] == "피카츄":
            self.my_pok.setPixmap(QPixmap("피카츄.png"))
        elif self.GP[0] == "파이리":
            self.my_pok.setPixmap(QPixmap("파이리.jpeg"))
        elif self.GP[0] == "꼬부기":
            self.my_pok.setPixmap(QPixmap("꼬부기.jpeg"))
        elif self.GP[0] == "이상해씨":
            self.my_pok.setPixmap(QPixmap("이상해씨.jpeg"))
        else:
            pass

    def go_adv(self):
        Battle_page().show()
        self.close()
    def go_pok_c(self):
        self.MPHp = self.Bhp
        pok_center().show()
    def go_quit(self):
        self.close()


class Battle_page(QMainWindow):
    EP = ['구구', '꼬렛', '꼬리선', '모다피', '주벳', '잉어킹']
    EPn = EP[random.randrange(len(EP))]
    def __init__(self):
        global Lvl, Bhp, potion, MPHp, EPHp, Mid, Mad, EPBa, MPBa, EPHp1
        super().__init__()
        self.loadUi = uic.loadUi("battle_main.ui",self)
        self.enemy_name.setText(f"{self.EPn}   Lv. {Lvl}")
        self.my_name.setText(f"{Game_Start().GP[0]}   Lv. {Lvl}")
        self.my_pic.setPixmap(Game_Start().my_pok.pixmap())
        if self.EPn == "구구":
            self.enemy_pic.setPixmap(QPixmap("구구.jpeg"))
        elif self.EPn == "꼬렛":
            self.enemy_pic.setPixmap(QPixmap("꼬렛.jpeg"))
        elif self.EPn == "꼬리선":
            self.enemy_pic.setPixmap(QPixmap("꼬리선.jpeg"))
        elif self.EPn == "모다피":
            self.enemy_pic.setPixmap(QPixmap("모다피.jpeg"))
        elif self.EPn == "주벳":
            self.enemy_pic.setPixmap(QPixmap("주벳.jpeg"))
        elif self.EPn == "잉어킹":
            self.enemy_pic.setPixmap(QPixmap("잉어킹.jpeg"))
        else:
            pass

        self.battle_info.setText(f"야생의 {self.EPn}(을)를 만났다!!\n{Game_Start().GP[0]}(은)는 무엇을할까?")
        self.my_HP.setMaximum(Bhp)
        self.enemy_HP.setMaximum(EPHp)
        self.fight.clicked.connect(self.go_fight)
        # self.potion.clicked.connect()
        self.run.clicked.connect(self.go_run)

    def go_fight(self):
        global Lvl, Bhp, potion, MPHp, EPHp, Mid, Mad, EPBa, MPBa, EPHp1
        Fn = random.randrange(0, 2)
        print(Fn)
        if Fn == 0:
            EPHp1 -= MPBa
            if 0 < EPHp1:
                self.battle_info.append(f"{Game_Start().GP[0]}이(가) 공격합니다!\n{MPBa}의 데미지를 주었습니다.")
                self.battle_info.append(f"{self.EPn}의 체력이 {EPHp1} 남았습니다!")
            elif EPHp1 <= 0:
                self.battle_info.append(f"{Game_Start().GP[0]}이(가) 공격합니다!\n{self.EPn}의 체력이 0이 되었습니다.")
                Lvl += 1
                Bhp += int(Bhp * (random.randint(5, 10) / 100))
                EPHp += int(Bhp * (random.randint(5, 10) / 100) * 7 / 10)
                Mid += int(Mid * random.randint(5, 10) / 100)
                Mad += int(Mid * (random.randint(5, 10) / 100))
                Pn = random.randrange(0, 2)
                self.battle_info.append(f"{Game_Start().GP[0]}(이)가 승리했습니다!!")
                if Pn == 0:
                    potion += 1
                    self.battle_info.append(f"포션을 한개 획득했습니다!\n현재포션 : {potion}개")
                    self.close()
                    Game_Start().show()
                elif Pn == 0:
                    self.close()
                    Game_Start().show()
        elif Fn == 1:
            MPHp -= EPBa
            if 0 < MPHp:
                self.battle_info.append(f"{self.EPn}이(가) 공격합니다!\n{EPBa}의 데미지를 주었습니다.")
                self.battle_info.append(f"{Game_Start().GP[0]}의 체력이 {MPHp} 남았습니다!")
            if MPHp <= 0:
                self.battle_info.append(f"{self.EPn}이(가) 공격합니다!\n{Game_Start().GP[0]}의 체력이 0이 되었습니다.")
                Lvl -= 1
                Bhp -= int(Bhp * (random.randint(5, 10) / 100))
                EPHp -= int(Bhp * (random.randint(5, 10) / 100) * 7 / 10)
                Mid -= int(Mid * random.randint(5, 10) / 100)
                Mad -= int(Mid * (random.randint(5, 10) / 100))
                self.battle_info.append(f"{Game_Start().user}는 눈앞이 깜깜해졌다...")
                MPHp = Bhp
                self.close()
                Game_Start().show()

    # def go_potion(self):
    #     global Lvl, Bhp, potion, MPHp, EPHp, Mid, Mad, EPBa, MPBa



    def go_run(self):
        global Lvl, Bhp, potion, MPHp, EPHp, Mid, Mad, EPBa, MPBa
        Game_Start().show()
        self.close()

class pok_center(QDialog):
    def __init__(self):
        super().__init__()
        self.loadUi = uic.loadUi("pokcenter.ui", self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Start()
    myWindow.show()
    app.exec()
