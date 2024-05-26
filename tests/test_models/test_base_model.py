#!/usr/bin/python3
"""
This file contains all the test cases for the Basemodel Class
"""


import unittest
from datetime import datetime
from models.base_model import BaseModel
import models


class TestBaseModel(unittest.TestCase):
    """
    Here is a list of the probable test Cases for BaseModel
    """

    def setUp(self):
        """
        Set up a new instance of BaseModel for testing.
        """
        self.instance = BaseModel()

    def tearDown(self):
        """
        tear down test environment if necessary
        """
        pass

    def test_initialization(self):
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

    def test_initialization_from_kwargs(self):
        """
        Test initialization from a dictionary representation
        """
        data = {
                'id': '1234',
                'created_at': '2024-05-17T12:34:56.789012',
                'updated_at': '2024-05-17T12:34:56.789012',
                'name': 'Test'
        }
        self.instance = BaseModel(**data)
        self.assertEqual(self.instance.id, '1234')
        self.assertEqual(
                self.instance.created_at, datetime.fromisoformat(
                    '2024-05-17T12:34:56.789012'))
        self.assertEqual(
                self.instance.updated_at, datetime.fromisoformat(
                    '2024-05-17T12:34:56.789012'))
        self.assertEqual(self.instance.name, 'Test')

    def test_invalid_datetime_kwargs_format(self):
        """
        Handling invalid datetime format in dict representation
        """
        data = {
                'id': '1234',
                'created_at': 'invalid_date',
                'updated_at': 'invalide_date',
                'name': 'Test'
        }
        with self.assertRaises(ValueError):
            self.instance = BaseModel(**data)

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

        self.instance.name = "Test"
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

    def test_str(self):
        """
        test the __str_ method ensuring it returns correct string repr
        """

        self.assertEqual(
            str(self.instance),
            f"[BaseModel] ({self.instance.id}) {self.instance.__dict__}"
        )


if __name__ == "__main__":
    unittest.main()
