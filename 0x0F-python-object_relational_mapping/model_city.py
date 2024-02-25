#!/usr/bin/python3
"""This module defines the class `City` of table `state` of the database."""

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
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
