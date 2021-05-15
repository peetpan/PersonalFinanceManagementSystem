import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import mysql.connector
import database


class DeleteExpense(QMainWindow):
    def __init__(self):
        super(DeleteExpense, self).__init__()
        loadUi("deleteexpense.ui", self)
        self.btn_delete.clicked.connect(self.delete)

    def delete(self):
        srno = int(self.srno.text())
        database.deleteexpense(srno)
        self.hide()


# app = QApplication(sys.argv)
# newface = DeleteExpense()
# newface.show()
# app.exec_()
