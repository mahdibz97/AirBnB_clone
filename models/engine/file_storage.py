#!/usr/bin/python3
""" Class file storage """
import json
from os import path
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """ serializes / deserializes an instances:
     file path :: JSON file path (string)
     objects :: store all objects (dictionary) """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ return dictionnary of objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        new = {}
        for i in self.all():
            new[i] = self.all()[i].to_dict()
        with open(self.__file_path, mode='w') as file:
            file.write(json.dumps(new))

    def reload(self):
        """  deserializes the JSON file to __objects """
        try:
            with open(self.__file_path) as file:
                data = json.load(file)
                for i, j in data.items():
                    k = i.split(".")[0]
                    obj = eval(k)(**j)
                    self.new(obj)
        except Exception:
            pass
