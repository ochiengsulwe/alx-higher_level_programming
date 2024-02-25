#!/usr/bin/python3
"""Creates the State "California".
With the City "San Francisco" in the database hbtn_0e_100_usa.
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

def create_california(username: str, password: str, database: str) -> None:
    """Creates the State "California" with the 
    City "San Francisco" in the specified database.

    Args:
        username (str): The username for the MySQL database.
        password (str): The password for the MySQL database.
        database (str): The name of the MySQL database.

    Returns:
        None
    """

    db_conn = f"mysql://{username}:{password}@localhost:3306/{database}"
    engine = create_engine(db_conn)
    Base.metadata.create_all(engine)


    Session = sessionmaker(bind=engine)
    session = Session()


    california = State(name="California")
    session.add(california)
    session.flush()


    san_francisco = City(name="San Francisco", state_id=california.id)
    session.add(san_francisco)


    session.commit()
    print("State 'California' with City 'San Francisco' created successfully.")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    create_california(username, password, database)
