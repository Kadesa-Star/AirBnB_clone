"""
    This file contains all the test cases for the Basemodel Class
"""


import unittest
from models.basemodel import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """ Here is a list of the probable test Cases for BaseModel """
    
    def setUp(self):
        """
        Set up a new instance of BaseModel for testing.
        """
        self.instance = BaseModel()

    def test_initialiation(self):
        """
        Tests to ensure BaseModel has the correct attributes upon initialization """

        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsNotNone(instance.id)
        self.assertIsNotNone(instance.created_at)
        self.assertIsNotNone(instance.updated_at)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_save(self):
        """ test the save method ensuring it updates teh updated_at attribute """

        prev_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(prev_updated_at, instance.updated_at)
        self.assertLess(prev_updated_at, instance.updated_at)

    def test_str(self):
        """
        test the __str_ method ensuring it returns correct string representation
        """

        self.assertEqual(str(instance), f"[BaseModel] ({instance.id} {instance.__dict__}")

    def test_to_dict(self):
        """
        Test the todict method ensuring it returns a dict with correct keys
        and values, including correctly formatted datetime attributes.
        """

        dict_instance = instance.to_dict()
        # check if the resulf is a dictionary
        self.assertIsInstance(dict_instance, dict)
        # check if the "__class__" is present and correct
        self.assertInt("__class__", dict_instance)
        self.assertEqual(dict_instance["__class__"], "BaseModel")
        # check if id is present and correct
        self.assertIn("id", dict_instance)
        self.assertEqual(dict_instance["id"], instance.id)
        # check if created_at is present and format is okay
        self.assertIn("created_at", dict_instance)
        self.assertEqual(dict_instance["created_at"], instance.created_at.isoformat())
        # check if updated_at is present and format is okay
        self.assertIn("updated_at", dict_instance)
        self.assertEqual(dict_instance["updated_at"], instance.updated_at.isoformat())

    # check if other attributes match the instance's __dict__
    for key, value in instance.__dict__.items():
        if key not in ["created_at", "updated_at"]:
            self.assertEqual(dict_instance[key], value)


    def test_init_with_kwargs(self):
        """
        test the __init__ method to ensure it correctly initializes an instance 
        when provided with a dictionary of attributes (kwargs).
        """

        data = {
                "id": "247",
                "created_at": "2024-05-14T12:00:00.000000",
                "updated_at": "2024-05-14T13:00:00.000000",
                "name": "Test"
                }
        instance = BaseModel(**data)

        # checking if id is set correctly
        self.assertEqual(instance.id, "247")
        # created_at converted to datetime obj and correctly set
        self.assertEqual(instance.created_at, datetime.fromisoformat("2024-05-14T12:00:00.000000"))
        # updated_at converted to datetime obj and correctly set
        self.assertEqual(instance.updated_at, datetime.fromisoformat("2024-05-14T13:00:00.000000"))
        # checking if custom attributtes are set correctly
        self.assertEqual(instance.name, "Test")


if __name__ == "__main__":
    unittest.main()
