#!/usr/bin/python3
"""This is the Base Class all other  classes inherit from it"""


import uuid
from datetime import datetime


class BaseModel:
    """this class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialize the Base Model
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.fromisoformat(value)
                if key != "__class__":
                    setattr(self, key, value)
        else:
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
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
        }
        return to_json
