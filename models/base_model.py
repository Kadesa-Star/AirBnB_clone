#!/usr/bin/python3
"""This is the Base Class all other  classes inherit from it"""


import uuid
from datetime import datetime


class BaseModel:
    """this class defines all common attributes/methods for other classes"""

    def __init__(self):
        """
        Initialize the Base Model
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Return a dictionary representation of instance
        """
        to_json = {
            '__class__': self.__class__.__name__,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        return to_json
