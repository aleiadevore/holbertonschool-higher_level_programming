#!/usr/bin/python3
""" adds the State object California with city "San Francisco" to the database hbtn_0e_6_usa """

import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    ed_state = State(name="California")
    ed_state.cities = [City(name="San Francisco")]
    session.add(ed_state)
    session.commit()
    