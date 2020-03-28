#!/usr/bin/python3
""" This module is used to list all the states from the database hbtn_0e_0_usa
    filtering by user input. This file is safe from SQL injections.

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
    cursor.execute(

        """SELECT id, name
        FROM cities
        WHERE state_id IN ( SELECT id
                            FROM states
                            WHERE name = %s)
        ORDER BY id ASC""", (sys.argv[4],))

    cities = cursor.fetchall()
    for i in range (0, len(cities)):
        if i + 1 != len(cities):
            print(cities[i][1], end=", ")
        else:
            print(cities[i][1])

    cursor.close()
    db.close()
