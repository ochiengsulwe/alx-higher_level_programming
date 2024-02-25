#!/usr/bin/python3
"""Prints the first `State`  object from the database `hbtn_0e_6_usa`.

If the database is empty, it will print "Nothing".
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def print_first(username: str, password: str, database: str) -> None:
    """Prints the first item in the states.

    Args:
        username: The name of the querying user.
        password: The password of the querying user to access the database.
        database: The databse we are querying.

    Returns:
        None: If at least an entry, prints the first entry
                else, prints string "Nothing".
    """
    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    print_first(username, password, database)
