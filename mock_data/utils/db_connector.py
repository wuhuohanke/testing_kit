import mysql.connector


def connect_to_db(database_name):
    conn = mysql.connector.connect(user="aaaa", password="bbbb", host="1.2.3.4", port="4321",
                                   database=database_name)
    return conn
