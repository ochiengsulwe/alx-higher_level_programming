#!/usr/bin/python3
"""Changes name of a state object in the database `hbtn_0e_6_usa`"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State


def change_name(username: str, password: str, database: str) -> None:
    """Changes the name of the State.

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

    state = session.query(State).filter_by(id=2).first()

    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    change_name(username, password, database)
