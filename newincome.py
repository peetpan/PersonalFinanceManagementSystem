import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import mysql.connector
import database


class NewIncome(QMainWindow):
    def __init__(self):
        super(NewIncome, self).__init__()
        loadUi("newincome.ui", self)
        self.btn_add.clicked.connect(self.add)

    def add(self):
        amount = int(self.amount.text())
        date = (self.date.date()).toPyDate()
        des = self.description.text()
        # print(amount,date,des)
        database.insertincome(amount, date, des)
        # Main.loadexpense()
        self.hide()


# app = QApplication(sys.argv)
# newface = NewExpense()
# newface.show()
# app.exec_()
