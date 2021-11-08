import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

import pandas as pd
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

page1 = uic.loadUiType("test.ui")[0]

class MainWindow(QMainWindow, page1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn.clicked.connect(self.gload)
        self.btn_2.clicked.connect(self.gload2)

        canvas = FigureCanvas()
        vbox = QVBoxLayout(self.widget)
        vbox.addWidget(canvas)
        self.ax = canvas.figure.subplots()


    def gload(self):
        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

        money = [1213, 2546, 3787, 4587, 1667, 7797, 5144, 8796]

        BabyDataset = list(zip(dayday, money))
        print(BabyDataset)

        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        y = df['money']
        x = df['day']

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.figure.canvas.draw()

    def gload2(self):
        dayday = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17',
                  '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31']

        money = [4555, 5146, 8787, 1587, 4567, 797, 1144, 3796, 4567, 6666, 7777, 1111, 2222, 3333]

        BabyDataset = list(zip(dayday, money))


        df = pd.DataFrame(data=BabyDataset, columns=['day', 'money'])

        y = df['money']
        x = df['day']

        self.ax.clear()
        self.ax.plot(x, y)
        self.ax.figure.canvas.draw()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    app.exec_()
