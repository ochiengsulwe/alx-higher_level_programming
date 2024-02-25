#!/usr/bin/python3
"""The script lists all `State` objects from the database `hbtn_0e_6_usa`"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def print_states(username: str, password: str, database: str) -> None:
    """Prints  all state objects from the states table.

        Args:
            username: The username of the db current user.
            password: The user password to allow for connection to database.
            database: The database we are querying.

        Returns:
            None: Prints queried results to the standard output.
    """

    conn_db = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(conn_db)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    print_states(username, password, database)

    Base.metadata.creat_all(engine)

    session.close()
