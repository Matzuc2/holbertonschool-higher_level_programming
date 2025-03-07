#!/usr/bin/python3
""" Start link class to table in database """
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    session = Session(engine)
    stmt = session.query(City, State)\
        .filter(City.state_id == State.id).order_by(City.id)
    for row in stmt:
        print("{}: ({}) {}".format(row.State.name, row.City.id, row.City.name))
    session.close()
