#!/usr/bin/python3
"""
  Create the class State which represent the table states
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
      table states for database
      __tablename__: the name of table
      id: the state id
      name: the state name
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}: {}".format(self.id, self.name)
