#!/usr/bin/python3
"""This module defines the class `State` of table `state` of the database."""

from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from model_state import Base


class City(Base):
    """City class represents a `city` table in the database."""
    __tablename__ = 'cities'

    def __repr__(self):
        """String represantation of the State object."""
        return f"<City(id={self.id}, name='{self.name}')>"

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


db_details = "mysql://username:password@localhost:3306/database_name"
engine = create_engine(db_details)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
