#!/usr/bin/python3
"""
The class inherits from the BaseModel
"""
from model.base_model import BaseModel


class User(BaseModel):
    """
    The user class inherits its properties from BaseModel
    """
    email = ""
    password = ""
    First_name = ""
    Last_name = ""

    def __init__(self, *arg, **kwargs):
        """
        The init function for user
        """
        super().__init__(*arg, **kwargs)
