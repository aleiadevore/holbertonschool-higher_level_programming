#!/usr/bin/python3
""" This module selects all states with user input """

import MySQLdb
import sys

if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], host="localhost", port=3306)
        c = db.cursor()
        cmd = "SELECT * FROM states WHERE name LIKE '{}' \
                ORDER BY id ASC".format(sys.argv[4])
        c.execute(cmd)
        q_rows = c.fetchall()
        for row in q_rows:
                if row[0] == 'N':
                        print(row)
        c.close()
        db.close()
