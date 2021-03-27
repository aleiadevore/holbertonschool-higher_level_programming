#!/usr/bin/python3
""" This model creates a States class """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
        """ This creates class from table states """

        __tablename__ = "states"

        id = Column(Integer, autoincrement=True, default=1,
                    unique=True, nullable=False, primary_key=True)

        name = Column(String(128), nullable=False)
