#!/usr/bin/python3
""" This module is used to list all the states from the database hbtn_0e_0_usa
    filtering by user input. This file is safe from SQL injections.

    Arguments:
            → Argv[0] = Function name.
            → ARGV[1] = MySQL user.
            → ARGV[2] = MySQL Password.
            → ARGV[3] = MySQL database.
            → ARGV[4] = State to filter.
"""

if __name__ == "__main__":

    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], port=3306,
                         host="localhost", db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(

        """SELECT cities.name
        FROM cities INNER JOIN states
        ON states.id = state_id
        WHERE states.name=%s""", (sys.argv[4],))

    cities = cursor.fetchall()

    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
