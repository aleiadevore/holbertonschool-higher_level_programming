#!/usr/bin/python3
""" This model creates a City class """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
        """ This creates class from table cities """

        __tablename__ = "cities"

        id = Column(Integer, autoincrement=True,
                    unique=True, nullable=False, primary_key=True)

        name = Column(String(128), nullable=False)

        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
