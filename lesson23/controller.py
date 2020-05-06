import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5 import QtCore, QtGui, QtWidgets
import myui


class MyCalc(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = myui.Ui_MainWindow()
        self.ui.setupUi(self)