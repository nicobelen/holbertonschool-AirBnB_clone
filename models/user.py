#!/usr/bin/python3

"""User"""

from models.base_model import BaseModel


class User(BaseModel):
    """initialization of class"""
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""
