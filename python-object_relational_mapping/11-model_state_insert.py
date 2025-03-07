#!/usr/bin/python3
""" Start link class to table in database """
from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import Session

from sqlalchemy import (create_engine)
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    session = Session(engine)
    new_user = State(name="Louisiana")
    session.add(new_user)
    session.commit()
    print("{}".format(new_user.id))
