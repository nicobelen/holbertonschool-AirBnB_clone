#!/usr/bin/python3

"""primary class BaseModel"""


import sys
from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseModel():
    """instantiation of user"""
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "created_at":
                    self.created_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    @classmethod
    def save(self):
        """atribute save"""
        dateobj = datetime.utcnow()
        self.updated_at = dateobj.strftime("%Y-%m-%dT%H:%M:%S.%f")
        
    def __str__(self):
        """atribute str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def to_dict(self):
        """returns a dictionary containing all keys and values"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__["__class__"] = self.__class__.__name__
        return (self.__dict__)
