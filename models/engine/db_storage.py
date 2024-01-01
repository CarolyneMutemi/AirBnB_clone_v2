#!/usr/bin/python3

"""
Contains the DBStorage class.
"""

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """
    Links to the database.
    """
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, pwd, host, db),
                                      pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    @staticmethod
    def query(clas, query):
        """
        Queries objects from the database using the query given.
        """
        dictionary = {}
        for obj in query:
            dictionary[f'{clas.__name__}.{obj.id}'] = obj
        return dictionary

    def all(self, cls=None):
        """
        Queries on the current database session all objects
        depending on the class name(cls).
        """
        dictionary = {}
        if cls:
            return DBStorage.query(cls, self.__session.query(cls))
        list_classes = ['State', 'City', 'User', 'Place', 'Review', 'Amenity']
        for clas in list_classes:
            cls = eval(clas)
            dictionary.update(DBStorage.query(cls, self.__session.query(cls)))
        return dictionary

    def new(self, obj):
        """
        Adds the object(obj) to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes to the database.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session.
        """
        if obj:
            clas = obj.__class__.__name__
            self.__session.query(clas).filter(eval(clas).id == obj.id).delete()
            self.__session.commit()

    def reload(self):
        """
        Reloads data.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
    
    def close(self):
        """
        Close function.
        """
        self.__session.close()
