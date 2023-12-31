#!/usr/bin/env python3
"""Module containig Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class Initializes review instances"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
