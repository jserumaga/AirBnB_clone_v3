#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv, name
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship

if getenv("HBNB_TYPE_STORAGE") == "db":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place")
else:
    class City(BaseModel):
        '''Class City for FileStorage'''
        name = ""
        state_id = ""
