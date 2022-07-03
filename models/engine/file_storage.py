#!/usr/bin/python3
"""Serializes instances to a JSON file and
deserializes JSON file to instances"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """initialization of FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """writes an object to a textfile"""
        odict = FileStorage.__objects
        aux = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(aux, f)

    def reload(self):
        """creates an object from a “JSON file”"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.loads(f.read())
        except Exception:
            pass
