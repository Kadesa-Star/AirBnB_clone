#!/usr/bin/python3
"""
The Class FileStorage serializes instances to JSON
and deserializes JSON file to instances
"""

import json
from os.path import exists
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file
    and deserializes JSON file to instance
    """

    CLASSES = {'BaseModel': BaseModel}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        this returns the dictionary
        we will be percolating the dict using the new methods
        it is like a getter
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"

        self.__objects[key] = obj

    def save(self):
        """
        we will use this method to persist in a file storage
        """
        serial_obj = {}
        for k, v in self.__objects.items():
            serial_obj[k] = v.to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(serial_obj, file, indent=2)

    def reload(self):
        """
        Deserializes the JSON file to __objects, if the JSON file exists.
        """
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as file:
                contents = json.load(file)
                for k, v in contents.items():
                    nombre_clase = v['__class__']

                    # here we are dynamically mapping the class
                    if nombre_clase in self.CLASSES:
                        instance = self.CLASSES[nombre_clase](**v)
                        self.__objects[k] = instance
