#!/usr/bin/python3
""" This module safely selects all states beginning with user input """

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                     host="localhost", port=3306)
c = db.cursor()
inpt = sys.argv[4]
newinpt = ""
for i in range(len(inpt)):
        if i != 0 and (inpt[i] == '\'' or inpt[i] == '\"'):
                break
        else:
                newinpt += inpt[i]
cmd = "SELECT * FROM states RIGHT JOIN cities ON states.id = cities.state_id WHERE states.name LIKE '{}'".format(newinpt)
c.execute(cmd)
q_rows = c.fetchall()
for row in q_rows:
        print(row)
c.close()
db.close()
