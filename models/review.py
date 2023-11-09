#!/usr/bin/python3
"""
The review inherits its properties from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    The class for users review
    """

    place_id = ""
    user_id = ""
    text = ""
