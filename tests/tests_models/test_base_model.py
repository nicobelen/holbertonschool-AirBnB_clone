#!/usr/bin/python3
"""Unit test for BaseModel"""

import unittest

from models.base_model import BaseModel

import pycodestyle

from datetime import datetime

from models.engine.file_storage import FileStorage

from os import path

class BaseModelTest(unittest.TestCase):

    """Test for BaseModel"""



    def test_pep8_base(self):

        """check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors"
        )
