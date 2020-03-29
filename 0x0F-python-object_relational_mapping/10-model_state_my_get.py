#!/usr/bin/python3
""" This module is used to list all the states from the database hbtn_0e_6_usa
    filtering by user input.

    Arguments:
            → Argv[0] = Function name.
            → ARGV[1] = MySQL user.
            → ARGV[2] = MySQL Password.
            → ARGV[3] = MySQL database.
            → ARGV[4] = Name to Search.
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    counter = 0

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    session = sessionmaker(bind=engine)
    States = session().query(State).all()

    for row in States:
        if row.name == sys.argv[4]:
            print(row.id)
            counter += 1

    if counter == 0:
        print("Not found")
