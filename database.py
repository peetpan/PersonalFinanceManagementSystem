import mysql.connector
from PyQt5 import QtWidgets


def totalexpense():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        query = """ select sum(amount) from expense"""
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result[0][0]
        # cursor.close()
        # connection.close()

    except mysql.connector.Error as error:
        print(f"Failed {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def totalincome():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        query = """ select sum(amount) from income"""
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        return result[0][0]
        # cursor.close()
        # connection.close()

    except mysql.connector.Error as error:
        print(f"Failed {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def insertexpense(amount, date, description):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        query = """insert into expense(amount, date, des) values (%s,%s,%s)"""
        insert_tuple = (amount, date, description)
        result = cursor.execute(query, insert_tuple)
        connection.commit()
        print("inserted successfully in the table", result)

    except mysql.connector.Error as error:
        print("Failed {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def deleteexpense(srno):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """DELETE from expense where sr = %s"""
        cursor.execute(sql_fetch_blob_query, (srno,))
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to delete data from MySQL table {} ".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

def insertincome(amount, date, description):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        query = """insert into income(amount, date, des) values (%s,%s,%s)"""
        insert_tuple = (amount, date, description)
        result = cursor.execute(query, insert_tuple)
        connection.commit()
        print("inserted successfully in the table", result)

    except mysql.connector.Error as error:
        print("Failed {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def deleteincome(srno):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='pfms',
                                             user='root',
                                             password='svvm1234')

        cursor = connection.cursor()
        sql_fetch_blob_query = """DELETE from income where sr = %s"""
        cursor.execute(sql_fetch_blob_query, (srno,))
        connection.commit()

    except mysql.connector.Error as error:
        print("Failed to delete data from MySQL table {} ".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")