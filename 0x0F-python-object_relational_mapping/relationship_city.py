#!/usr/bin/python3
"""
  module for class city
"""

from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
      class represent the table cities
      __tablename__: name of table
      name: name of city
      id: id of city
      state_id: forein key to state.id
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"))
