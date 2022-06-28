#!/usr/bin/python3

"""promary class BaseModel"""

from calendar import formatstring
from locale import format_string
import sys
from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseModel():
    """instantiation of user"""
    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4()
        self.created_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f")

    
    @classmethod
    def save(self):
        """atribute save"""
        dateobj = datetime.utcnow()
        self.updated_at = dateobj.strftime("%Y-%m-%dT%H:%M:%S.%f")
        
    def __str__(self):
        """atribute str"""
        print("print de str")
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def to_dict(self):
        """returns a dictionary containing all keys and values"""
        print("print de to_dict")
        return{"id": {self.id}, "created_at": {self.created_at}, "updated_at": {self.updated_at}, "__class__": self.__class__.__name__}
