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

    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    session = sessionmaker(bind=engine)()

    States = session.query(City, State).filter(
        State.id == City.state_id).order_by(City.id).all()

    for city, state in States:
        print("{}: ({}) {}  ".format(state.name, city.id, city.name))
    session.close()
