#!/usr/bin/python3
""" This module lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                     host="localhost", port=3306)
c = db.cursor()
c.execute("""SELECT * FROM states ORDER BY id ASC""")
q_rows = c.fetchall()
for row in q_rows:
        print(row)
c.close()
db.close()
