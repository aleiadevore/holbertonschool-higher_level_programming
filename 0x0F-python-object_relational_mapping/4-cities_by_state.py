#!/usr/bin/python3
""" This module prints all cities and states """

import MySQLdb
import sys

if __name__ == "__main__":
        db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3], host="localhost", port=3306)
        c = db.cursor()
        c.execute("""SELECT cities.id, cities.name, states.name from cities INNER JOIN
                states ON cities.state_id = states.id ORDER BY cities.id""")
        q_rows = c.fetchall()
        for row in q_rows:
                print(row)
        c.close()
        db.close()
