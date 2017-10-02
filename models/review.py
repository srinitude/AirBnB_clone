#!/usr/bin/python3
"""
Class Review that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """
    Class Review that inherits from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
