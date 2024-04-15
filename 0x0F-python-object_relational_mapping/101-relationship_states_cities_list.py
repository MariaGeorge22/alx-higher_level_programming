#!/usr/bin/python3

'''
lists all cities from the database hbtn_0e_0_usa
'''

from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (asc, create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).order_by(asc(State.id)).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("	{}: {}".format(city.id, city.name))
