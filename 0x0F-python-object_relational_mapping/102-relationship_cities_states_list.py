#!/usr/bin/python3
""" Lists all City objects and corresponding State """

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

    places = session.query(City).order_by(City.id).all()
    for row in places:
        print("{}: {} -> {}".format(row.id, row.name, row.state.name))
    session.close()
