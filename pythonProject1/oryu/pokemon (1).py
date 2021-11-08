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

class pokemon:
    op_gif = ["'../_qt_ui/gif/op/1/op1.gif'", "'../_qt_ui/gif/op/1/op2.gif'", "'../_qt_ui/gif/op/1/op3.gif'",\
           "'../_qt_ui/gif/op/2/op1.gif'", "'../_qt_ui/gif/op/2/op2.gif'", "'../_qt_ui/gif/op/2/op3.gif'", "'../_qt_ui/gif/op/2/op4.gif'", "'../_qt_ui/gif/op/2/op5.gif'",\
           \
           "'../_qt_ui/gif/op/3/op1.gif'", "'../_qt_ui/gif/op/3/op2.gif'", "'../_qt_ui/gif/op/3/op3.gif'", "'../_qt_ui/gif/op/3/op4.gif'", "'../_qt_ui/gif/op/3/op5.gif'",\
           "'../_qt_ui/gif/op/3/op6.gif'", "'../_qt_ui/gif/op/3/op7.gif'", "'../_qt_ui/gif/op/3/op8.gif'", "'../_qt_ui/gif/op/3/op9.gif'", "'../_qt_ui/gif/op/3/op10.gif'",\
           \
           "'../_qt_ui/gif/op/4/op1.gif'", "'../_qt_ui/gif/op/4/op2.gif'", "'../_qt_ui/gif/op/4/op3.gif'", "'../_qt_ui/gif/op/4/op4.gif'", "'../_qt_ui/gif/op/4/op5.gif'",\
           "'../_qt_ui/gif/op/4/op6.gif'", "'../_qt_ui/gif/op/4/op7.gif'", "'../_qt_ui/gif/op/4/op8.gif'", "'../_qt_ui/gif/op/4/op9.gif'", "'../_qt_ui/gif/op/4/op10.gif'",\
           \
           "'../_qt_ui/gif/op/5/op1.gif'","'../_qt_ui/gif/op/5/op2.gif'","'../_qt_ui/gif/op/5/op3.gif'","'../_qt_ui/gif/op/5/op4.gif'","'../_qt_ui/gif/op/5/op5.gif'",\
           "'../_qt_ui/gif/op/5/op6.gif'","'../_qt_ui/gif/op/5/op7.gif'","'../_qt_ui/gif/op/5/op8.gif'","'../_qt_ui/gif/op/5/op9.gif'","'../_qt_ui/gif/op/5/op10.gif'"]
    # 1 = [0] ~ [2]
    # 2 = [3] ~ [7]
    # 3 = [8] ~ [17]
    # 4 = [18] ~ [27]
    # 5 = [28] ~ [37]

    my_level = ["Lv. 1 피카츄", "Lv. 2 피카츄", "Lv. 3 피카츄", "Lv. 4 피카츄",\
             "Lv. 1 파이리", "Lv. 2 파이리", "Lv. 3 파이리", "Lv. 4 파이리",\
             "Lv. 1 꼬부기", "Lv. 2 꼬부기", "Lv. 3 꼬부기", "Lv. 4 꼬부기",\
             "Lv. 1 이상해씨", "Lv. 2 이상해씨", "Lv. 3 이상해씨", "Lv. 4 이상해씨"]
    # [0] ~ 0
    # [4] ~ 4 5 7
    # [8] ~ 8 9 11
    # [12] ~ 12 13 15
    # print(my_level[2])

########################################################################################################################
class poke4(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(UI4, self)

        self.pushButton_hp.setStyleSheet('image:url(../_qt_ui/icon/icon_hp48.png);')
        self.pushButton_mp.setStyleSheet('image:url(../_qt_ui/icon/icon_mp48.png);')
        # a = poke3()
        # print(a.label_pokemon_name.text())


        # op_random = randint(0)
        # level_num = re.findall(r'\d+', self.label_my.text())
        # level_num = level_num[0]
        # if level_num == 1:
        #     o = QMovie("../_qt_ui/gif/op/1/op1.gif")
        #     self.label_oppokemon.setMovie(o)
        #     o.start()

        num_min, num_max = 0, 100
        num_value_hp = 100
        num_value_mp = 100
        # 나의 HP, MP
        self.progressBar_hp.setAlignment(Qt.AlignCenter)
        self.progressBar_hp.setRange(num_min, num_max)
        self.progressBar_hp.setValue(num_value_hp)

        self.progressBar_mp.setAlignment(Qt.AlignCenter)
        self.progressBar_mp.setRange(num_min, num_max)
        self.progressBar_mp.setValue(num_value_mp)
        # 상대 HP, MP
        self.progressBar_op_hp.setAlignment(Qt.AlignCenter)
        self.progressBar_op_hp.setRange(num_min, num_max)
        self.progressBar_op_hp.setValue(num_value_hp)

        self.progressBar_op_mp.setAlignment(Qt.AlignCenter)
        self.progressBar_op_mp.setRange(num_min, num_max)
        self.progressBar_op_mp.setValue(100)

        # 스킬 4, 5 버튼 잠금
        self.pushButton_skill4.setEnabled(False)
        self.pushButton_skill5.setEnabled(False)

        self.pushButton_back.clicked.connect(self.back)
        # self.pushButton_skill1.clicked.connect(lambda state, skill1 = , skill2 = , skill3 =  : self.skill1(state, skill1, skill2, skill3))
        # self.pushButton_skill2.clicked.connect(lambda state, skill1 = , skill2 = , skill3 =  : self.skill2(state, skill1, skill2, skill3))
        # self.pushButton_skill1.clicked.connect(lambda state, skill1 = , skill2 = , skill3 =  : self.skill3(state, skill1, skill2, skill3))

    ### SIGNAL #########################################################################################################
    def back(self):
        self.poke3 = poke3()
        # print(self.label_my.text())
        self.poke3.show()
        self.close()
    # def skill(self, state, skill1, skill2, skill3):
    #     self.progressBar_op_hp.setValue()
    # while True:

########################################################################################################################
class poke3(QMainWindow):
    my_level = ["Lv. 1 피카츄", "Lv. 2 피카츄", "Lv. 3 피카츄", "Lv. 4 피카츄",\
             "Lv. 1 파이리", "Lv. 2 파이리", "Lv. 3 파이리", "Lv. 4 파이리",\
             "Lv. 1 꼬부기", "Lv. 2 꼬부기", "Lv. 3 꼬부기", "Lv. 4 꼬부기",\
             "Lv. 1 이상해씨", "Lv. 2 이상해씨", "Lv. 3 이상해씨", "Lv. 4 이상해씨"]

    op_gif = ["'../_qt_ui/gif/op/1/op1.gif'", "'../_qt_ui/gif/op/1/op2.gif'", "'../_qt_ui/gif/op/1/op3.gif'",\
           "'../_qt_ui/gif/op/2/op1.gif'", "'../_qt_ui/gif/op/2/op2.gif'", "'../_qt_ui/gif/op/2/op3.gif'", "'../_qt_ui/gif/op/2/op4.gif'", "'../_qt_ui/gif/op/2/op5.gif'",\
           \
           "'../_qt_ui/gif/op/3/op1.gif'", "'../_qt_ui/gif/op/3/op2.gif'", "'../_qt_ui/gif/op/3/op3.gif'", "'../_qt_ui/gif/op/3/op4.gif'", "'../_qt_ui/gif/op/3/op5.gif'",\
           "'../_qt_ui/gif/op/3/op6.gif'", "'../_qt_ui/gif/op/3/op7.gif'", "'../_qt_ui/gif/op/3/op8.gif'", "'../_qt_ui/gif/op/3/op9.gif'", "'../_qt_ui/gif/op/3/op10.gif'",\
           \
           "'../_qt_ui/gif/op/4/op1.gif'", "'../_qt_ui/gif/op/4/op2.gif'", "'../_qt_ui/gif/op/4/op3.gif'", "'../_qt_ui/gif/op/4/op4.gif'", "'../_qt_ui/gif/op/4/op5.gif'",\
           "'../_qt_ui/gif/op/4/op6.gif'", "'../_qt_ui/gif/op/4/op7.gif'", "'../_qt_ui/gif/op/4/op8.gif'", "'../_qt_ui/gif/op/4/op9.gif'", "'../_qt_ui/gif/op/4/op10.gif'",\
           \
           "'../_qt_ui/gif/op/5/op1.gif'","'../_qt_ui/gif/op/5/op2.gif'","'../_qt_ui/gif/op/5/op3.gif'","'../_qt_ui/gif/op/5/op4.gif'","'../_qt_ui/gif/op/5/op5.gif'",\
           "'../_qt_ui/gif/op/5/op6.gif'","'../_qt_ui/gif/op/5/op7.gif'","'../_qt_ui/gif/op/5/op8.gif'","'../_qt_ui/gif/op/5/op9.gif'","'../_qt_ui/gif/op/5/op10.gif'"]

    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(UI3, self)

        num_min, num_max = 0, 100
        num_value_hp = 100
        num_value_mp = 100
        num_value_ex = 0

        self.progressBar_hp.setAlignment(Qt.AlignCenter)
        self.progressBar_hp.setRange(num_min, num_max)
        self.progressBar_hp.setValue(num_value_hp)

        self.progressBar_mp.setAlignment(Qt.AlignCenter)
        self.progressBar_mp.setRange(num_min, num_max)
        self.progressBar_mp.setValue(num_value_mp)

        self.progressBar_ex.setAlignment(Qt.AlignCenter)
        self.progressBar_ex.setRange(num_min, num_max)
        self.progressBar_ex.setValue(num_value_ex)

        # w = int(self.label_hp.width())
        # h = int(self.label_hp.height())
        self.label_hp.setPixmap(
            QPixmap('../_qt_ui/icon/icon_hp48.png'))
        self.label_mp.setPixmap(
            QPixmap('../_qt_ui/icon/icon_mp48.png'))

        self.pushButton_fight.clicked.connect(self.fight)
        self.progressBar_ex.valueChanged.connect(self.valuechanged)

    ### SIGNAL #########################################################################################################
    def valuechanged(self):
        self.progressBar_ex.reset()

    ### SIGNAL #########################################################################################################
    def fight(self):
        self.poke4 = poke4()
        # 프로필페이지 포켓몬 이름 전투페이지 나의 포켓몬 이름으로
        self.poke4.label_my.setText(self.label_pokemon_name.text())
        # print(self.label_pokemon_name.text())
        # print(self.poke4.label_my.text())

        # op = randint(0, 2)
        # num = re.findall(r'\d+', self.poke4.label_my.text())
        # print(self.poke4.label_my.text())
        # num = num[0]
        # print(num)

        # 피카츄
        if self.label_pokemon_name.text() == poke3.my_level[0]:
            m = QMovie("../_qt_ui/poke/m/p1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()

        # 파이리
        elif self.label_pokemon_name.text() == poke3.my_level[4]:
            m = QMovie("../_qt_ui/poke/m/f1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[5]:
            m = QMovie("../_qt_ui/poke/m/f2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[7]:
            m = QMovie("../_qt_ui/poke/m/f3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        # 꼬부기
        elif self.label_pokemon_name.text() == poke3.my_level[8]:
            m = QMovie("../_qt_ui/poke/m/k1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[9]:
            m = QMovie("../_qt_ui/poke/m/k2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[11]:
            m = QMovie("../_qt_ui/poke/m/k3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        # 이상해씨
        elif self.label_pokemon_name.text() == poke3.my_level[12]:
            m = QMovie("../_qt_ui/poke/m/e1.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[13]:
            m = QMovie("../_qt_ui/poke/m/e2.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()
        elif self.label_pokemon_name.text() == poke3.my_level[15]:
            m = QMovie("../_qt_ui/poke/m/e3.gif")
            self.poke4.label_mypokemon.setMovie(m)
            m.start()

        num = re.sub(r'[^0-9]', '', self.poke4.label_my.text())
        print(num)
        print(type(num))
        
        if int(num) == 1:
            op = QMovie(poke3.op_gif[1])
            self.poke4.label_oppokemon.setMovie(op)
            op.start()

        self.poke4.show()
        self.close()

    # def display(self):
    #     self.get = poke1()
    #     self.get.valuesend.connect(self.get_Value)
    #
    # @pyqtSlot(str)
    # def get_Value(self, text):
    #     print(text)

########################################################################################################################
class poke_potion(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        loadUi(UI_potion, self)

########################################################################################################################
class poke2(QDialog):
    name = ["Lv. 1 피카츄", "Lv. 1 파이리", "Lv. 1 꼬부기", "Lv. 1 이상해씨"]
    def __init__(self):
        QDialog.__init__(self)
        loadUi(UI2, self)

        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_back.clicked.connect(self.back)

    ### SIGNAL #########################################################################################################
    def next(self):
        self.poke3 = poke3()
        self.poke3.label_player_name.setText(self.lineEdit.text())
        self.poke3.label_pokemon_name.setText(self.label_pokemon_name.text())
        if self.label_pokemon_name.text() == poke2.name[0]:
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/p/Pikachu.png);')
            p1 = QMovie("../_qt_ui/poke/p/p1.gif")
            self.poke3.label_pokemon1.setMovie(p1)
            p1.start()
        elif self.label_pokemon_name.text() == poke2.name[1]:
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/f/Charmander.png);')
            f1 = QMovie("../_qt_ui/poke/f/f1.gif")
            self.poke3.label_pokemon1.setMovie(f1)
            f1.start()
            f2 = QMovie("../_qt_ui/poke/f/f2.gif")
            self.poke3.label_pokemon2.setMovie(f2)
            f2.start()
            f3 = QMovie("../_qt_ui/poke/f/f3.gif")
            self.poke3.label_pokemon3.setMovie(f3)
            f3.start()
        elif self.label_pokemon_name.text() == poke2.name[2]:
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/k/Squirtle.png);')
            k1 = QMovie("../_qt_ui/poke/k/k1.gif")
            self.poke3.label_pokemon1.setMovie(k1)
            k1.start()
            k2 = QMovie("../_qt_ui/poke/k/k2.gif")
            self.poke3.label_pokemon2.setMovie(k2)
            k2.start()
            k3 = QMovie("../_qt_ui/poke/k/k3.gif")
            self.poke3.label_pokemon3.setMovie(k3)
            k3.start()
        else :
            self.poke3.label_mypokemon.setStyleSheet('image:url(../_qt_ui/poke/e/Bulbasaur.png);')
            e1 = QMovie("../_qt_ui/poke/e/e1.gif")
            self.poke3.label_pokemon1.setMovie(e1)
            e1.start()
            e2 = QMovie("../_qt_ui/poke/e/e2.gif")
            self.poke3.label_pokemon2.setMovie(e2)
            e2.start()
            e3 = QMovie("../_qt_ui/poke/e/e3.gif")
            self.poke3.label_pokemon3.setMovie(e3)
            e3.start()

        self.poke3.show()
        pokemon.close()
        self.close()

    ### SIGNAL #########################################################################################################
    def back(self):
        pokemon.show()
        self.close()

    ### SIGNAL #########################################################################################################
    def modal(self):
        self.setModal(True)
        self.show()

class poke1(QDialog):
    # valuesend = pyqtSignal(str)
    def __init__(self):
        QDialog.__init__(self)
        loadUi(UI1, self)

        # w = int(self.label_ppp.width())
        # h = int(self.label_ppp.height())
        # size = QSize(w, h)
        p = (QMovie("../_qt_ui/poke/p/p1.gif"))
        self.label_ppp.setMovie(p)
        p.start()
        # 파이리 gif
        f = (QMovie("../_qt_ui/poke/f/f1.gif"))
        self.label_fff.setMovie(f)
        f.start()
        # 꼬부기 gif
        k = (QMovie("../_qt_ui/poke/k/k1.gif"))
        self.label_kkk.setMovie(k)
        k.start()
        # 이상해씨 gif
        e = (QMovie("../_qt_ui/poke/e/e1.gif"))
        self.label_eee.setMovie(e)
        e.start()


        self.pushButton_ppp.clicked.connect(lambda state, pokemon = "Lv. 1 피카츄" : self.profile(state, pokemon))
        self.pushButton_fff.clicked.connect(lambda state, pokemon = "Lv. 1 파이리" : self.profile(state, pokemon))
        self.pushButton_kkk.clicked.connect(lambda state, pokemon = "Lv. 1 꼬부기" : self.profile(state, pokemon))
        self.pushButton_eee.clicked.connect(lambda state, pokemon = "Lv. 1 이상해씨" : self.profile(state, pokemon))

    ### SIGNAL #########################################################################################################
    def profile(self, state, pokemon):
        # self.valuesend.emit("피카츄")
        self.poke2 = poke2()
        self.poke2.label_pokemon_name.setText(pokemon)
        self.poke2.modal()
        # self.poke3 = poke3()
        # self.poke3.label_pokemon_name.setText(pokemon)
        # poke1().isEnabled(True)
        # pokemon.setVisible(False)

########################################################################################################################
IlovePython = QApplication(sys.argv)
pokemon = poke1()
pokemon.show()
IlovePython.exec()