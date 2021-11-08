import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

UI1 = 'pokemon1.ui'
UI2 = 'pokemon2.ui'
UI3 = 'pokemon3.ui'
UI4 = 'pokemon4.ui'

class poke4(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI4, self)

class poke3(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI3, self)

        num_min, num_max = 0, 100
        num_value_hp = 90
        num_value_mp = 90
        num_value_ex = 90

        self.progressBar_hp.setAlignment(Qt.AlignCenter)
        self.progressBar_hp.setRange(num_min, num_max)
        self.progressBar_hp.setValue(num_value_hp)
        # self.progressBar_hp.setFormat("HP " + str(num_value_hp))
        # self.progressBar_hp.setTextVisible(False)
        # print(self.progressBar_hp.text())

        self.progressBar_mp.setAlignment(Qt.AlignCenter)
        self.progressBar_mp.setRange(num_min, num_max)
        self.progressBar_mp.setValue(num_value_mp)
        # self.progressBar_mp.setFormat("MP " + str(num_value_mp))

        self.progressBar_ex.setAlignment(Qt.AlignCenter)
        self.progressBar_ex.setRange(num_min, num_max)
        self.progressBar_ex.setValue(num_value_ex)
        # self.progressBar_ex.setFormat("EX " + str(num_value_ex))

        self.pushButton_fight.clicked.connect(self.fight)

    def fight(self):
        self.poke4 = poke4()
        self.poke4.show()
        self.close()

class poke2(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI2, self)

        self.pushButton_next.clicked.connect(self.next)
        self.pushButton_back.clicked.connect(self.back)

    def next(self):
        self.poke3 = poke3()
        self.poke3.label_player_name.setText(self.lineEdit.text())
        self.poke3.show()
        pokemon.close()
        self.close()

    def back(self):
        pokemon.show()
        self.close()

class poke1(QMainWindow):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(UI1, self)

        # w = int(self.label_ppp.width())
        # h = int(self.label_ppp.height())
        # size = QSize(w, h)
        self.ppp = (QMovie("ppp.gif"))
        # self.ppp.setScaledSize(size)
        self.label_ppp.setMovie(self.ppp)
        self.ppp.start()
        # 파이리 gif
        self.fff = (QMovie("fff.gif"))
        self.label_fff.setMovie(self.fff)
        self.fff.start()
        # 꼬부기 gif
        self.kkk = (QMovie("kkk.gif"))
        self.label_kkk.setMovie(self.kkk)
        self.kkk.start()
        # 이상해씨 gif
        self.eee = (QMovie("eee.gif"))
        self.label_eee.setMovie(self.eee)
        self.eee.start()

        self.pushButton_ppp.clicked.connect(self.profile)
        self.pushButton_ppp.clicked.connect(self.name)
        self.pushButton_fff.clicked.connect(lambda state, pokemonname = "파이리" : self.profile(state, pokemonname))
        self.pushButton_kkk.clicked.connect(lambda state, pokemonname = "꼬부기" : self.profile(state, pokemonname))
        self.pushButton_eee.clicked.connect(lambda state, pokemonname = "이상해씨" : self.profile(state, pokemonname))

    def name(self):
        self.poke3 = poke3()
        self.poke3.label_pokemon_name.setText("hi")

    def profile(self):
        self.poke2 = poke2()
        self.poke2.show()
    #     self.setEnabled(True)
        # pokemon.setVisible(False)


IlovePython = QApplication(sys.argv)
pokemon = poke1()
pokemon.show()
IlovePython.exec_()