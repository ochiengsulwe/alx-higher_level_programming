#!/usr/bin/python3
"""Delets all entries having letter 'a' from the database `hbtn_0e_6_usa`."""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def deletes_with_a(username: str, password: str, database: str) -> None:
    """Deletes items in the states table having a letter 'a'.

    Args:
        username: The name of the querying user.
        password: The password of the querying user to access the database.
        database: The databse we are querying.

    Returns:
        None:
    """
    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_with_a = (
        session.query(State)
        .filter(State.name.like('%a%'))
        .all()
       )

    if state_with_a:
        for state in state_with_a:
            session.delete(state)
        session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    deletes_with_a(username, password, database)
