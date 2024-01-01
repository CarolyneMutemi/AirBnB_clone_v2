#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()

from models.base_model import BaseModel

#class Base():
#    pass
#
#from models.user import User
#from models.amenity import Amenity
#from models.city import City
#from models.place import Place
#from models.state import State
#from models.review import Review
#from models.engine import file_storage
#
#
#storage = file_storage.FileStorage()
#storage.reload()
