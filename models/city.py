#!/usr/bin/env python3
"""Module containing City class"""
from models.base_model import BaseModel


class City(BaseModel):
    """This initializes City instances"""
    state_id: str = ""
    name: str = ""
