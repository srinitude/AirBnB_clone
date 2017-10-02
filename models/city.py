#!/usr/bin/python3
"""
Class City that inherits from BaseModel
"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    """
    Class City that inherits from BaseModel
    """
    state_id = ""
    name = ""
