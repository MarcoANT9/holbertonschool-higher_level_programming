#!/usr/bin/python3
""" This module is used to list all the states from the database hbtn_0e_0_usa.
    Arguments:
            → Argv[0] = Function name.
            → ARGV[1] = MySQL user.
            → ARGV[2] = MySQL Password.
            → ARGV[3] = MySQL database.
"""

import MySQLdb
import sys


def select_states():
    """ This function select all the states in a database in ascending order.
        The program will always connect via the port 3306.                """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306,
                         host="localhost", db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()
