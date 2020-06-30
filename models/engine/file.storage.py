#!/usr/bin/python3
""" Class file storage """
import json
from os import path


class FileStorage:
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
        if obj:
            key = obj["__class__"] + '.' + obj["id"]
            setattr(self.__objects, key, self.obj)

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        with open(self.__file_path, mode='w') as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """  deserializes the JSON file to __objects """
        if path.exists(__file_path):
            with open(self.__file_path) as file:
                self.__objects = json.load(file)
