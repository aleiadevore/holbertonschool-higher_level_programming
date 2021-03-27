#!/usr/bin/python3
""" This module selects all states beginning with 'N' """

import MySQLdb
import sys

if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], host="localhost", port=3306)
        c = db.cursor()
        c.execute("""SELECT * FROM states WHERE name \
                   LIKE 'N%' ORDER BY id ASC""")
        q_rows = c.fetchall()
        for row in q_rows:
                print(row)
        c.close()
        db.close()
