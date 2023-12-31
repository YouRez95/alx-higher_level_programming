#!/usr/bin/python3
"""
  get the id of state
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name == sys.argv[4]).all()
    if len(results) == 0:
        print("Not found")
    else:
        print(results[0].id)
