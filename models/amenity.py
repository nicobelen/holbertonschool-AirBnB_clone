#!/usr/bin/python3
"""City Amety"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Instantation of class Amenity"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ class constructor """

        super().__init__(*args, **kwargs)
