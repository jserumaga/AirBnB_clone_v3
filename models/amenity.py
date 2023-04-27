#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


if getenv("HBNB_TYPE_STORAGE") == "db":
    class Amenity(BaseModel, Base):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        # place_amenities = relationship("Place")
else:
    class Amenity(BaseModel):
        '''Create class Amenity'''
        name = ""
