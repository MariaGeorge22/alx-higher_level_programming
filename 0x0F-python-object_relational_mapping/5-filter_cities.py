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
    state = args[4]
    c.execute(
        """SELECT cities.name
        from cities JOIN states
        WHERE states.id = cities.state_id AND states.name = %s
        ORDER BY cities.id""", (state,))
    rows = c.fetchall()
    rows_formatted = list(map(lambda tub: tub[0], rows))
    print(", ".join(rows_formatted))
    # Close the connection
    db.close()
