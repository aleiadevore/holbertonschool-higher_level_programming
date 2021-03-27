#!/usr/bin/python3
""" This module lists first State object from the database hbtn_0e_6_usa """

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

""" Filtering user input (state) to prevent injection """
inpt = sys.argv[4]
newinpt = ""
for i in range(len(inpt)):
        if i != 0 and (inpt[i] == '\'' or inpt[i] == '\"'):
                break
        else:
                newinpt += inpt[i]

""" Filtering and printing """
Session = sessionmaker(bind=engine)
session = Session()
for item in session.query(State).filter(State.name.like
                                        (inpt)).order_by(State.id):
    print(item.id)
"""else:
    print("Not found")"""
