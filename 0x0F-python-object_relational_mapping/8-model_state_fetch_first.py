#!/usr/bin/python3
"""
  fectch all state ordered by id and limitid by 1 row
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
    results = session.query(State).limit(1)
    # print(results)
    if not results:
        print("Nothing")
    for r in results:
        print(r)
