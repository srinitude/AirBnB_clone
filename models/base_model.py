#!/usr/bin/python3
"""
Lays out the properties and behavior of a BaseModel
"""

import uuid
import datetime


class BaseModel:
    """
    Lays out the properties and behavior of a BaseModel
    """
    def __init__(self):
        """
        Initializer of a BaseModel
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """
        The pretty String representation of a BaseModel
        """
        base_class_name = self.__class__.__name__
        base_id = self.id
        base_dict = self.__dict__
        return "[{}] ({}) {}".format(base_class_name, base_id, base_dict)

    def save(self):
        """
        Updates the 'updated_at' property with the current datetime
        """
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = str(new_dict["created_at"])
        new_dict["updated_at"] = str(new_dict["updated_at"])
        return new_dict
