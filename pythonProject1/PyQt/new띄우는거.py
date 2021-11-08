import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("new.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.yap)
        self.listWidget.itemDoubleClicked.connect(self.mm)




    def yap(self):
        self.listWidget.addItem("얍")

    def mm(self):
        self.removeItemRow = self.listWidget.currentRow()
        self.listWidget.takeItem(self.removeItemRow)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()