#!/usr/bin/python3
"""This is the Base Class all other  classes inherit from it"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """this class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialize the Base Model
        """
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, t_format))
                else:
                    setattr(self, k, v)
        else:
            models.storage.new(self)

    def save(self):
        """
        update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of instance
        """
        this_dict = self.__dict__.copy()
        this_dict['__class__'] = self.__class__.__name__
        this_dict['created_at'] = self.created_at.isoformat()
        this_dict['updated_at'] = self.updated_at.isoformat()
        return this_dict

    def __str__(self):
        """ this returns the string repr of basemodel instance """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
