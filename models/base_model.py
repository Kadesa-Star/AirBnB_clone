#!/usr/bin/python3
"""This is the Base Class all other  classes inherit from it"""

import uuid
from datetime import datetime
import models


class BaseModel:
    """this class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """
        Initialize the Base Model
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.fromisoformat(v)
                if k != "__class__":
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        update the updated_at attribute with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return a dictionary representation of instance
        """
        this_dict = self.__dict__
        this_dict['__class__'] = self.__class__.__name__
        this_dict['created_at'] = self.created_at.isoformat()
        this_dict['updated_at'] = self.updated_at.isoformat()
        return this_dict
