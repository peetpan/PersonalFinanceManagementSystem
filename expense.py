import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow, QFileDialog
from PyQt5.uic import loadUi
import mysql.connector
import database


class Expense(QMainWindow):
    def __init__(self):
        super(Expense, self).__init__()
        loadUi("expense.ui", self)
        self.btn_load.clicked.connect(self.loadexpense)

    def loadexpense(self):
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

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed")


app = QApplication(sys.argv)
newface = Expense()
newface.show()
app.exec_()
