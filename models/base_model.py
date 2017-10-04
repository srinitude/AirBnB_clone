#!/usr/bin/python3
"""
Lays out the properties and behavior of a BaseModel
"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Lays out the properties and behavior of a BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        Initializer of a BaseModel
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs):
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
        models.storage.new(self)
        models.storage.save()

    def __setattr__(self, attr, value):
        """
        Lets BaseModel handle type casting
        """
        fmt = "%Y-%m-%dT%H:%M:%S.%f"

        if attr == "created_at" and type(value) is str:
            self.created_at = datetime.strptime(value, fmt)
        elif attr == "updated_at" and type(value) is str:
            self.updated_at = datetime.strptime(value, fmt)
        else:
            super().__setattr__(attr, value)

    def __str__(self):
        """
        The pretty String representation of a BaseModel
        """
        class_name = self.__class__.__name__
        obj_id = self.id
        obj_dict = self.__dict__
        return "[{}] ({}) {}".format(class_name, obj_id, obj_dict)

    def save(self):
        """
        Updates the 'updated_at' property with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__ of instance
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
