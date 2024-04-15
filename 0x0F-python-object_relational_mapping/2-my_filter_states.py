#!/usr/bin/python3

'''
lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect("localhost", args[1], args[2], args[3])
    name = args[4]
    c = db.cursor()
    c.execute(
        'SELECT * from states WHERE states.name LIKE \
          BINARY "{}" ORDER BY states.id'.format(name))
    rows = c.fetchall()
    for row in rows:
        print(row)
    # Close the connection
    db.close()
