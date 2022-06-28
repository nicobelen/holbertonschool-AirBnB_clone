"""Serializes instances to a JSON file and deserializes JSON file to instances"""


from base_model import BaseModel


class FileStorage(BaseModel):
    """initialization of FileStorage"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__file_path = 