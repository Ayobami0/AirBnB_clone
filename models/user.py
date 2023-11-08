#!/usr/bin/python3
"""
The class inherits from the BaseModel
"""
from model.base_model import BaseModel


class User(BaseModel):
    """
    The user class inherits its properties from BaseModel
    """
    Email = ""
    password = ""
    FirstName = ""
    LastName = ""

    def __init__(self arg, **kargs)
    """
    The init function for user
    """
    super().__init__(*arg, **kwargs)
