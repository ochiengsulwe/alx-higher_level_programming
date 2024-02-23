#!/usr/bin/python3
"""This module defines the class `State` of table `state` of the database."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class State(Base):
    """State class represents a `state` table in the database."""
    __tablename__ = 'states'

    def __repr__(self):
        """String represantation of the State object."""
        return f"<State(id={self.id}, name='{self.name}')>"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://username:password@localhost:3306/database_name')

if __name__ == "__main__":
    Base.metadata.create_all(engine)
