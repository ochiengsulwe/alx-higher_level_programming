#!/usr/bin/python3
"""Fetches all City objects from the database hbtn_0e_14_usa."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City
from model_state import Base, State


def fetch_cities_by_state(username: str, password: str, database: str) -> None:
    """
    Fetches and prints all City objects from the specified database.

    Args:
        username: The username for the MySQL database.
        password: The password for the MySQL database.
        database: The name of the MySQL database.

    Returns:
        None
    """
    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = (
                session.query(State.name)
                .filter_by(id=city.state_id)
                .scalar()
               )
        print(f"{state_name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    fetch_cities_by_state(username, password, database)
