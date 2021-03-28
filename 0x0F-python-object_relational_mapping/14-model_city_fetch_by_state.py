#!/usr/bin/python3
""" This module lists all City objects from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    places = session.query(State, City).filter(
        State.id, State.id == City.state_id).order_by(State.id)
    for state, city in places:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
