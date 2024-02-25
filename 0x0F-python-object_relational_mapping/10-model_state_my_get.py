#!/usr/bin/python3
"""Prints the `State` object.

With name passed as argument from the database `hbtn_0e_6_usa`.
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def print_name(username: str, password: str, database: str, name: str) -> None:
    """Prints the State object containing 'name'.

    Args:
        username: The name of the querying user.
        password: The password of the querying user to access the database.
        database: The databse we are querying.
        name: The name to check if is in database.

    Returns:
        None: If at least an entry, prints the first entry
                else, prints string "Not found".
    """
    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = (
        session.query(State)
        .filter(State.name == name)
        .first()
       )

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    name = sys.argv[4]

    print_name(username, password, database, name)
