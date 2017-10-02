#!/usr/bin/python3
"""
Serializes instances to a JSON file and deserializes
JSON file to instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes
    JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to JSON file
        """
        new_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict = obj.to_dict()
            new_dict[key] = obj_dict
        with open(FileStorage.__file_path, "w") as fs:
            json.dump(new_dict, fs)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        try:
            with open(FileStorage.__file_path, "r") as fs:
                obj_dicts = json.load(fs)
                for key, d in obj_dicts.items():
                    class_name = d["__class__"]
                    new_obj = eval(class_name)(**d)
                    FileStorage.__objects[key] = new_obj
        except FileNotFoundError:
            return
