import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import mysql.connector
import database
from deleteexpense import DeleteExpense
from deleteincome import DeleteIncome
from newexpense import NewExpense
from newincome import NewIncome


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("main.ui", self)
        self.stackedWidget.setCurrentWidget(self.main_page)
        self.loadmain()
        self.btn_expense.clicked.connect(self.loadexpense)
        self.btn_income.clicked.connect(self.loadincome)
        self.btn_main.clicked.connect(self.loadmain)
        self.btn_newexpense.clicked.connect(self.loadnewexpense)
        self.btn_refreshexpense.clicked.connect(self.loadexpense)
        self.btn_deletexpense.clicked.connect(self.loaddeleteexpense)
        self.btn_newincome.clicked.connect(self.loadnewincome)
        self.btn_refreshincome.clicked.connect(self.loadincome)
        self.btn_deleteincome.clicked.connect(self.loaddeleteincome)

    def loadexpense(self):
        self.stackedWidget.setCurrentWidget(self.expense_page)
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='pfms',
                                                 user='root',
                                                 password='svvm1234')

            cursor = connection.cursor()
            query = """ SELECT * FROM expense"""
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            self.tableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
            print("SuccessDB", result)
            # cursor.close()
            # connection.close()

        except mysql.connector.Error as error:
            print(f"Failed {error}")

        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")
        total_expense = str(database.totalexpense())
        self.lbl_te.setText(total_expense)

    def loadincome(self):
        self.stackedWidget.setCurrentWidget(self.income_page)
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='pfms',
                                                 user='root',
                                                 password='svvm1234')

            cursor = connection.cursor()
            query = """ SELECT * FROM income"""
            cursor.execute(query)
            result = cursor.fetchall()
            connection.commit()
            self.incometableWidget.setRowCount(0)
            for row_number, row_data in enumerate(result):
                self.incometableWidget.insertRow(row_number)
                for col_number, data in enumerate(row_data):
                    self.incometableWidget.setItem(row_number, col_number, QtWidgets.QTableWidgetItem(str(data)))
            # print("SuccessDB", result)
            # cursor.close()
            # connection.close()

        except mysql.connector.Error as error:
            print(f"Failed {error}")

        # finally:
        #     if connection.is_connected():
        #         cursor.close()
        #         connection.close()
        #         print("MySQL connection is closed")
        total_income = str(database.totalincome())
        self.lbl_ti.setText(total_income)


    def loadmain(self):
        self.stackedWidget.setCurrentWidget(self.main_page)
        total_expense = str(database.totalexpense())
        total_income = str(database.totalincome())
        saving = str(int(total_income) - int(total_expense))
        self.lbl_expense.setText(total_expense)
        self.lbl_income.setText(total_income)
        self.lbl_saving.setText(saving)

    def loadnewexpense(self):
        self._new_window = NewExpense()
        self._new_window.show()

    def loaddeleteexpense(self):
        self._new_window = DeleteExpense()
        self._new_window.show()

    def loadnewincome(self):
        self._new_window = NewIncome()
        self._new_window.show()

    def loaddeleteincome(self):
        self._new_window = DeleteIncome()
        self._new_window.show()



app = QApplication(sys.argv)
window = Main()
window.show()
app.exec_()
