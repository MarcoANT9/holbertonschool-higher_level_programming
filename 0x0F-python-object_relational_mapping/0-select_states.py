#!/usr/bin/python3
""" This module is used to list all the states from the database hbtn_0e_0_usa.
    Arguments:
            → Argv[0] = Function name.
            → ARGV[1] = MySQL user.
            → ARGV[2] = MySQL Password.
            → ARGV[3] = MySQL database.
"""

if __name__ == "__main__":

    import MySQLdb
    import sys


    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306,
                         host="localhost", db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states ORDER BY id ASC""")
    for i in cursor.fetchall():
        print(i)

    cursor.close()
    db.close()
