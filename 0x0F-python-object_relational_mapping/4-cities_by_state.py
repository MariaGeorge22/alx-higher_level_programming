#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_0_usa
'''

import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv
    db = MySQLdb.connect("localhost", args[1], args[2], args[3])
    c = db.cursor()
    c.execute(
        """SELECT cities.id, cities.name, states.name
        from cities JOIN states WHERE states.id = cities.state_id
        ORDER BY cities.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    # Close the connection
    db.close()
