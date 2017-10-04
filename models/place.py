#!/usr/bin/python3
"""
Class Place that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.city import City
from models.user import User
from models.amenity import Amenity


class Place(BaseModel):
    """
    Class Place that inherits from BaseModel
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __setattr__(self, attr, value):
        """
        Lets Place handle type casting
        """
        if attr == "number_rooms" and type(value) is str:
            self.number_rooms = int(value)
        elif attr == "number_bathrooms" and type(value) is str:
            self.number_bathrooms = int(value)
        elif attr == "max_guest" and type(value) is str:
            self.max_guest = int(value)
        elif attr == "price_by_night" and type(value) is str:
            self.price_by_night = int(value)
        elif attr == "latitude" and type(value) is str:
            self.latitude = float(value)
        elif attr == "longitude" and type(value) is str:
            self.longitude = float(value)
        else:
            super().__setattr__(attr, value)
