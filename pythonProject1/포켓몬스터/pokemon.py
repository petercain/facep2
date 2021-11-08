import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *

UI1 = 'poke1.ui'
UI2 = 'poke2.ui'
UI3 = 'poke3.ui'
UI4 = 'poke4.ui'

class poke4(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(UI4, self)


class poke3(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(UI3, self)

        self.progressBar_ex.setMinimum(0)
        self.progressBar_ex.setMaximum(200)
        ex = 100
        self.progressBar_ex.setValue(ex)

        self.pushButton_fight.clicked.connect(self.fight)

    def fight(self):
        self.poke4 = poke4()
        self.poke4.show()
        self.close()

class poke2(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(UI2, self)

        self.pushButton_back.clicked.connect(self.back)
        self.pushButton_profile.clicked.connect(self.profile)

    def back(self):
        pokemon.show()
        self.close()

    def profile(self):
        self.poke3 = poke3()
        self.poke3.label_nickname.setText(self.lineEdit.text())
        self.poke3.show()
        self.close()


class poke1(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        loadUi(UI1, self)

        self.pushButton_kkk.clicked.connect(self.profile)
        self.pushButton_fff.clicked.connect(self.profile)
        self.pushButton_ppp.clicked.connect(self.profile)
        self.pushButton_eee.clicked.connect(self.profile)

    def profile(self):
        self.poke2 = poke2()
        self.poke2.show()
        self.close()


IlovePython = QApplication(sys.argv)
pokemon = poke1()
pokemon.show()
IlovePython.exec_()