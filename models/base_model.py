#!/usr/bin/python3
import json

class BaseModel:
    """this class defines all common attributes/methods for other classes"""
    

    def __init__(self, id, created_at, updated_at) -> None:
        self.id = str(id)
        self.created_at = str(created_at)
        self.updated_at = str(updated_at)

    def __str__(self) -> str:
        return f"id: {self.id} created_at: {self.created_at} updated_at: {self.updated_at}"

    # this returns a json object to dictionary
    def to_dict(self):
        to_json = self.__dict__
        return to_json

    # Serialization
    def save(self):
        with open('file.json', "w", indent = 2) as file:
            json.dump(self.__dict__(), file)




# instances of the class
User1 = Basemodel(45, june 1, june 2)
print(User1)
User1.save()


