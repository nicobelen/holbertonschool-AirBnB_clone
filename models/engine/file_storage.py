#!/usr/bin/python3
"""Serializes instances to a JSON file and
deserializes JSON file to instances"""


import json


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
            with open(FileStorage.__file_path) as f:
                aux = json.load(f)
                for o in aux.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
