#!/usr/bin/python3
"""Adds a new entry to the database `hbtn_0e_6_usa`."""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def add_entry(username: str, password: str, database: str) -> None:
    """Adds a new entry to my database.

    Args:
        username: The name of the querying user.
        password: The password of the querying user to access the database.
        database: The databse we are querying.

    Returns:
        None: Prints new state aftr entry.
    """
    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()

    print(louisiana.id)

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    add_entry(username, password, database)
