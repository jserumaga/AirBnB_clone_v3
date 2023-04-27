#!/usr/bin/python3

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.state import State
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.amenity import Amenity
# from models import *


class DBStorage:
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(user, pwd, host, db),
                                      pool_pre_ping=True)

        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Show all class objects in DB storage or specified class """
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        my_dict = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            classes = [cls]
        for j in classes:
            for k in self.__session.query(j).all():
                key = "{}.{}".format(type(k).__name__, k.id)
                my_dict[key] = k
        return my_dict

    def new(self, obj):
        '''Create a new object'''
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """dsdcsd """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create database in Alchemy"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker()
        Session.configure(bind=self.__engine)
        # Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        # Session = scoped_session(Session)
        self.__session = Session()

    def close(self):
        """ Close Session """
        self.__session.close()
