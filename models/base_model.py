#!/usr/bin/python3
import json
from uuid import uuid4
from datetime import datetime
import os

class BaseModel:
    """this class defines all common attributes/methods for other classes"""
    #serial_objc = {}
    def __init__(self) -> None:
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    
    # here we save our data in a file
    def save(self) -> None:
        self.updated_at = datetime.now()
    """
        self.serial_objc[self.new_k()] = self.to_dict()
        with open('file.json', "w", indent = 2) as file:
            json.dump(self.serial_objc, file)
    """

    # this returns a json object to dictionary
    def to_dict(self):
        to_json = self.__dict__
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = to_json['created_at'].isoformat()
        to_json['updated_at'] = to_json['updated_at'].isoformat()
        return to_json

    """def new_k(self):
        key = f"{self.__class__.__name__}.{self.id}"
        return key

    def reload(self):
        with open('file.json', "r", indent = 2) as file:
            if os.path.getsize('file.json') > 0:
                prev_data = json.load(file)
                # print(prev_data)
                    for i, j in prev_data.items():
                    self.serial_objc[i] = j
"""

# instances of the class
User1 = BaseModel()
print(User1)
#User1.reload()
#User1.save()


