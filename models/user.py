#!/usr/bin/env python3
"""Module containing User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class initializes user instances"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
