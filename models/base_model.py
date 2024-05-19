#!/usr/bin/python3
"""This is the Base Class all other  classes inherit from it"""
import uuid
from datetime import datetime


class BaseModel:
    """this class defines all common attributes/methods for other classes"""

    # serial_objc = {}
    def __init__(self):
        self.id = str(uuid4())
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
        to_json = self.__dict__.copy()
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = to_json['created_at'].isoformat()
        to_json['updated_at'] = to_json['updated_at'].isoformat()
        return to_json
