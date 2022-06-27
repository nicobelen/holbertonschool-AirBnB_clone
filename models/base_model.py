#!/usr/bin/python3

"""promary class BaseModel"""

import sys
from abc import ABC, abstractmethod
import uuid
from datetime import datetime

class BaseModel():
    """instantiation of user"""
    def __init__(self, *args, **kwargs):
        self.id = uuid.uuid4()
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    
    @classmethod
    def save(self):
        """atribute save"""
        self.updated_at = datetime.utcnow()
        
    def __str__(self):
        """atribute str"""
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def to_dict(self):
        """returns a dictionary containing all keys and values"""
        return{"id": {self.id}, "created_at": {self.created_at}, "updated_at": {self.updated_at}, "__class__": self.__class__.__name__}
