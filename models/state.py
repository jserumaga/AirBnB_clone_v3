#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from models.base_model import BaseModel, Base
import models
from models.city import City


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City')
else:
    class State(BaseModel):
        """ Defined class to work with FileStorage'"""
        name = ''
        cities = models.storage.all(City)

        @property
        def cities(self):
            citis_list = []
            cities = models.storage.all(City).values()
            for city in cities:
                if city.state_id == self.id:
                    citis_list.append(city)
            return citis_list
