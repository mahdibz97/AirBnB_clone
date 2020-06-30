#!/usr/bin/python3
"""BaseModel that defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime


class BaseModel():
    """class defines all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """ initialization of instance attribute
        id : unique id number of instance
        created_at : when an instance is created
        updated_at : when the last modification of an instance
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
           for i, j in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(j, "%Y-%m-%dT%H:%M:%S.%f")
                elif i == '__class__':
                    self.__class__.__name__ = j
                else:
                    setattr(self, i, j)

    def __str__(self):
        """magic method"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """ updates attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ returns a dictionary of the instance"""
        d = self.__dict__
        d.update(__class__=self.__class__.__name__)
        d.update(created_at=self.created_at.isoformat())
        d.update(updated_at=self.updated_at.isoformat())
        return d