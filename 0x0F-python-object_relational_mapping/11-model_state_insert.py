#!/usr/bin/python3
"""
  add state to database and print all states
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
    state = State("Louisiana")
    session.add(state)
    session.commit()
    state_added = session.query(State).filter_by(name='Louisiana').first()
    print(state_added.id)
    results = session.query(State).all()
    for r in results:
        print(r)
