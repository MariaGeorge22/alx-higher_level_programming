#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_0_usa
'''

from sqlalchemy.orm import sessionmaker
import sys
from model_state import Base, State
from sqlalchemy import (asc, create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).order_by(asc(State.id)).first()
    if row is None:
        print("Nothing")
    else:
        print("{}: {}".format(row.id, row.name))
