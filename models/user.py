#!/usr/bin/python3
"""This module defines a class User"""
from os import getenv
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


if getenv("HBNB_TYPE_STORAGE") == "db":
    class User(BaseModel, Base):
        """This class defines a user by various attributes"""
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)

        places = relationship("Place")
        reviews = relationship("Review")
else:
    class User(BaseModel):
        '''Defined class to work with FileStorage'''
        email = ''
        password = ''
        first_name = ''
        last_name = ''
