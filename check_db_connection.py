__author__ = 'ja'

import mysql.connector

connection = mysql.connector.connect(host="localhost", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list;")
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()
