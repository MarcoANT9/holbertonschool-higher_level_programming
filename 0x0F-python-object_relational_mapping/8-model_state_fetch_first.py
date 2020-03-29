#!/usr/bin/python3
""" This module is used to list all the first element from the database
    hbtn_0e_6_usa.

    Arguments:
            → Argv[0] = Function name.
            → ARGV[1] = MySQL user.
            → ARGV[2] = MySQL Password.
            → ARGV[3] = MySQL database.
"""

if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    session = sessionmaker(bind=engine)

    State = session().query(State).first()
    if State:
        print("{}: {}".format(State.id, State.name))
    else:
        print("Nothing")
