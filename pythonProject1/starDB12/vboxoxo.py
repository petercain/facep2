import sys
import time
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvas as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class MyApp(QMainWindow):

  def __init__(self):
      super().__init__()

#위젯 만들고 선언하고
      self.main_widget = QWidget()
      self.setCentralWidget(self.main_widget)
      btn1 = QPushButton('&Button1', self)

      btn1.clicked.connect(self.update_canvas)
#움직이는거 만든거고


      dynamic_canvas = FigureCanvas(Figure(figsize=(4, 3)))
      vbox = QVBoxLayout(self.main_widget)
      vbox.addWidget(dynamic_canvas)

      self.dynamic_ax = dynamic_canvas.figure.subplots()


#창띄우는거
      self.setWindowTitle('Matplotlib in PyQt5')
      self.setGeometry(300, 100, 600, 600)
      self.show()

  def update_canvas(self):
      self.dynamic_ax.clear()
      self.dynamic_ax.plot([0, 1, 2], [1, 5, 3], '-')
      self.dynamic_ax.figure.canvas.draw()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = MyApp()
  sys.exit(app.exec_())