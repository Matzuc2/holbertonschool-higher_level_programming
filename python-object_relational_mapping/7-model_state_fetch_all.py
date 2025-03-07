#!/usr/bin/python3
""" Start link class to table in database """
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy import MetaData
from sqlalchemy import select

from sqlalchemy import (create_engine)
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
metadata = MetaData(engine)

stmt = select(State)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print("{}: {}".format(row.id, row.name))
