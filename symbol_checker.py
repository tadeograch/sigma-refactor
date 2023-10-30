#!/usr/bin/python3
""" File containing the simbol checker function """

import pymysql as MySQLdb


MY_H = "localhost"
MY_U = "root"
MY_P = "root"
MY_D = "MySql80"

def symbol_checker(symbol):
    """ Function to check if a symbol is in the database """
    db = MySQLdb.connect(host=MY_H, user=MY_U, passwd=MY_P, db=MY_D)
    cur = db.cursor()
    cur.execute("SELECT * FROM symbols")
    for row in cur.fetchall():
        if row[0] == symbol:
            return True
    return False