#!/usr/bin/python3
"""
Lays out the properties and behavior of a BaseModel
"""

import uuid
from datetime import datetime


class BaseModel:
    """
    Lays out the properties and behavior of a BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer of a BaseModel
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "created_at" in kwargs:
                self.created_at = datetime.strptime(kwargs["created_at"], fmt)
            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(kwargs["updated_at"], fmt)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

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
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
