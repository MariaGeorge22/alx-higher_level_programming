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
    state = State(name="California")
    city = City(name="San Francisco")
    city.state = state
    state.cities.append(city)
    session.add_all([state, city])
    session.commit()
