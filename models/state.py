#!/usr/bin/env python3
"""Module containing State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """This class Initializes State instances"""
    name: str = ""
