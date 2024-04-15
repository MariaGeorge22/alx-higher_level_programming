#!/usr/bin/python3
"""
Module for City
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base, State


class City(Base):
    """
    City Class
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False,)
    state = relationship("State")
