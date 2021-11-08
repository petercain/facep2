import sys
import re

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic

CafeUI = 'sb.ui'

class variable:
    totalmoney = 0

class Cafe(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)
        uic.loadUi(CafeUI, self)

        self.pushButton_americano.clicked.connect(lambda state, menu = "아메리카노", hot = self.checkBox_americano_hot,
                                                         ice = self.checkBox_americano_ice,
                                                         spin = self.spinBox_americano, price = 2000 : self.menuclicked(state, menu, hot, ice, spin, price))
        self.pushButton_caramel.clicked.connect(lambda state, menu = "카라멜 마끼아또", hot = self.checkBox_caramel_hot,
                                                         ice = self.checkBox_caramel_ice,
                                                         spin = self.spinBox_caramel, price = 3500 : self.menuclicked(state, menu, hot, ice, spin, price))
        self.pushButton_hazelnuts.clicked.connect(lambda state, menu = "헤이즐넛", hot = self.checkBox_hazelnuts_hot,
                                                         ice = self.checkBox_hazelnuts_ice,
                                                         spin = self.spinBox_hazelnuts, price = 4000 : self.menuclicked(state, menu, hot, ice, spin, price))
        self.pushButton_cafelatte.clicked.connect(lambda state, menu = "카페라떼", hot = self.checkBox_cafelatte_hot,
                                                         ice = self.checkBox_cafelatte_ice,
                                                         spin = self.spinBox_cafelatte, price = 2500 : self.menuclicked(state, menu, hot, ice, spin, price))
        self.pushButton_cappuccino.clicked.connect(lambda state, menu = "카푸치노", hot = self.checkBox_cappuccino_hot,
                                                         ice = self.checkBox_cappuccino_ice,
                                                         spin = self.spinBox_cappuccino, price = 3000 : self.menuclicked(state, menu, hot, ice, spin, price))
        self.pushButton_moca.clicked.connect(lambda state, menu = "카페모카", hot = self.checkBox_moca_hot,
                                                         ice = self.checkBox_moca_ice,
                                                         spin = self.spinBox_moca, price = 3000 : self.menuclicked(state, menu, hot, ice, spin, price))

        self.pushButton_cancellation.clicked.connect(self.cancellationclicked)
        self.pushButton_order.clicked.connect(self.orderclicked)

        self.checkBox_americano_hot.clicked.connect(lambda state, hot = self.checkBox_americano_hot, ice = self.checkBox_americano_ice : self.hotclicked(state, hot, ice))
        self.checkBox_caramel_hot.clicked.connect(lambda state, hot = self.checkBox_caramel_hot, ice = self.checkBox_caramel_ice : self.hotclicked(state, hot, ice))
        self.checkBox_hazelnuts_hot.clicked.connect(lambda state, hot = self.checkBox_hazelnuts_hot, ice = self.checkBox_hazelnuts_ice : self.hotclicked(state, hot, ice))
        self.checkBox_cafelatte_hot.clicked.connect(lambda state, hot = self.checkBox_cafelatte_hot, ice = self.checkBox_cafelatte_ice : self.hotclicked(state, hot, ice))
        self.checkBox_cappuccino_hot.clicked.connect(lambda state, hot = self.checkBox_cappuccino_hot, ice = self.checkBox_cappuccino_ice : self.hotclicked(state, hot, ice))
        self.checkBox_moca_hot.clicked.connect(lambda state, hot = self.checkBox_moca_hot, ice = self.checkBox_moca_ice : self.hotclicked(state, hot, ice))

        self.checkBox_americano_ice.clicked.connect(lambda state, ice = self.checkBox_americano_ice, hot = self.checkBox_americano_hot : self.iceclicked(state, ice, hot))
        self.checkBox_caramel_ice.clicked.connect(lambda state, ice = self.checkBox_caramel_ice, hot = self.checkBox_caramel_hot : self.iceclicked(state, ice, hot))
        self.checkBox_hazelnuts_ice.clicked.connect(lambda state, ice = self.checkBox_hazelnuts_ice, hot = self.checkBox_hazelnuts_hot : self.iceclicked(state, ice, hot))
        self.checkBox_cafelatte_ice.clicked.connect(lambda state, ice = self.checkBox_cafelatte_ice, hot = self.checkBox_cafelatte_hot : self.iceclicked(state, ice, hot))
        self.checkBox_cappuccino_ice.clicked.connect(lambda state, ice = self.checkBox_cappuccino_ice, hot = self.checkBox_cappuccino_hot : self.iceclicked(state, ice, hot))
        self.checkBox_moca_ice.clicked.connect(lambda state, ice = self.checkBox_moca_ice, hot = self.checkBox_moca_hot : self.iceclicked(state, ice, hot))

        self.lineEdit_inputmoney.setText("0")
        self.label_totalmoney.setText("0")
        self.label_change2.setText("0")

    def menuclicked(self, state, menu, hot, ice, spin, price):
        if hot.isChecked() == False and ice.isChecked() == False:
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_starbucks.png"))
            msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_starbucks_48.png"))
            msgBox.setWindowTitle("Infomation")
            msgBox.setText("ICE / HOT을 선택해주세요.")
            msgBox.setInformativeText("STARBUCKS")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            return msgBox.exec_()
        elif spin.value() == 0:
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_starbucks.png"))
            msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_starbucks_48.png"))
            msgBox.setWindowTitle("Infomation")
            msgBox.setText("수량을 선택해주세요.")
            msgBox.setInformativeText("STARBUCKS")
            msgBox.setStandardButtons(QMessageBox.Ok)
            msgBox.setDefaultButton(QMessageBox.Ok)
            if hot.isChecked() == True:
                hot.setChecked(True)
            elif ice.isChecked() == True:
                ice.setChecked(True)
            msgBox.exec_()
        elif hot.isChecked() == True:
            menus = str(menu)
            self.listWidget_purchase.addItem(menus + "[{}]{}개{}원"
                                             .format(ice.text(), spin.value(),
                                                     price * spin.value()))
            hot.setChecked(False)
            ice.setEnabled(True)
            variable.totalmoney += price * spin.value()
            self.label_totalmoney.setText("{}".format(variable.totalmoney))
        elif ice.isChecked() == True:
            self.listWidget_purchase.addItem(menu + "[{}]{}개{}원"
                                             .format(ice.text(), spin.value(),
                                                     (price+300) * spin.value()))
            ice.setChecked(False)
            hot.setEnabled(True)
            variable.totalmoney += (price + 300) * spin.value()
            self.label_totalmoney.setText("{}".format(variable.totalmoney))
        spin.setValue(0)

    def cancellationclicked(self):
        try:
            onlynumber = re.findall(r'\d+', self.listWidget_purchase.currentItem().text())
            print(onlynumber)
            print(type(onlynumber))
            onlynumber = onlynumber[1]
            self.listWidget_purchase.takeItem(self.listWidget_purchase.currentRow())
            variable.totalmoney -= int(onlynumber)
            self.label_totalmoney.setText("{}".format(variable.totalmoney))
        except:
            pass

    def hotclicked(self, state, hot, ice):
        if hot.isChecked() == True:
            ice.setEnabled(False)
        else:
            ice.setEnabled(True)

    def iceclicked(self, state, ice, hot):
        if ice.isChecked() == True:
            hot.setEnabled(False)
            msgBox = QMessageBox()
            msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_starbucks.png"))
            msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_starbucks_48.png"))
            msgBox.setWindowTitle("Infomation")
            msgBox.setText("ICE 선택 시 300원이 추가됩니다.")
            msgBox.setInformativeText("STARBUCKS")
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.setDefaultButton(QMessageBox.Cancel)
            a = msgBox.exec_()
            if a == QMessageBox.Ok:
                ice.setChecked(True)
            elif a == QMessageBox.Cancel:
                ice.setChecked(False)
                hot.setEnabled(True)
        else:
            hot.setEnabled(True)

    def orderclicked(self):
        try:
            if self.label_totalmoney.text() == "0":
                self.label_totalmoney.setText("메뉴를 선택해주세요.")
            elif int(self.lineEdit_inputmoney.text()) < int(self.label_totalmoney.text()):
                msgBox = QMessageBox()
                msgBox.setWindowIcon(QIcon("../_qt_ui/icon/icon_starbucks.png"))
                msgBox.setIconPixmap(QPixmap("../_qt_ui/icon/icon_starbucks_48.png"))
                msgBox.setWindowTitle("Infomation")
                msgBox.setText("돈이 부족합니다.")
                msgBox.setInformativeText("STARBUCKS")
                msgBox.setStandardButtons(QMessageBox.Ok)
                msgBox.setDefaultButton(QMessageBox.Ok)
                msgBox.exec_()
            elif int(self.lineEdit_inputmoney.text()) >= int(self.label_totalmoney.text()):
                self.label_change2.setText("{}".format(int(self.lineEdit_inputmoney.text()) - int(self.label_totalmoney.text())))
                self.label_totalmoney.setText("주문이 완료 되었습니다.")
                self.listWidget_purchase.clear()
                self.lineEdit_inputmoney.setText("0")
            variable.totalmoney = 0
        except:
            pass

app = QApplication(sys.argv)
ch = Cafe()
ch.show()
app.exec_()