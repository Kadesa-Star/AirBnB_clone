#!/usr/bin/python3
"""
This file contains all the test cases for the Basemodel Class
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Here is a list of the probable test Cases for BaseModel
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel for testing.
        """
        self.instance = BaseModel()

    def test_initialiation(self):
        """
        Tests to ensure BaseModel has the correct attributes
        upon initialization
        """

        self.assertIsInstance(self.instance, BaseModel)
        self.assertIsInstance(self.instance.id, str)
        self.assertIsNotNone(self.instance.id)
        self.assertIsNotNone(self.instance.created_at)
        self.assertIsNotNone(self.instance.updated_at)
        self.assertIsInstance(self.instance.created_at, datetime)
        self.assertIsInstance(self.instance.updated_at, datetime)

    def test_str(self):
        """
        test the __str_ method ensuring it returns correct
        string representation
        """

        self.assertEqual(
                str(self.instance),
                f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        )

    def test_save(self):
        """
        test the save method ensuring it updates the
        updated_at attribute
        """

        prev_updated_at = self.instance.updated_at
        self.instance.save()
        self.assertNotEqual(prev_updated_at, self.instance.updated_at)
        self.assertLess(prev_updated_at, self.instance.updated_at)

    def test_to_dict(self):
        """
        Test the todict method ensuring it returns a dict with correct keys
        and values, including correctly formatted datetime attributes.
        """

        dict_instance = self.instance.to_dict()
        # check if the resulf is a dictionary
        self.assertIsInstance(dict_instance, dict)
        # check if the "__class__" is present and correct
        self.assertIn("__class__", dict_instance)
        self.assertEqual(dict_instance["__class__"], "BaseModel")
        # check if created_at is present and format is okay
        self.assertIn("created_at", dict_instance)
        self.assertEqual(
                dict_instance["created_at"],
                self.instance.created_at.isoformat()
        )
        # check if updated_at is present and format is okay
        self.assertIn("updated_at", dict_instance)
        self.assertEqual(
                dict_instance["updated_at"],
                self.instance.updated_at.isoformat()
        )

    # check if other attributes match the instance's __dict__
        for key, value in self.instance.__dict__.items():
            if key not in ["created_at", "updated_at"]:
                self.assertEqual(dict_instance[key], value)


if __name__ == "__main__":
    unittest.main()
