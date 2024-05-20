#!/usr/bin/python3
"""
This are the Test Cases for the file_storage
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class """

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.file_path = FileStorage._FileStorage__file_path
        self.objects = FileStorage._FileStorage__objects

    def tearDown(self):
        """Tear down the test environment"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        """Test that all returns the __objects dictionary"""
        self.assertEqual(self.storage.all(), self.objects)

    def test_new(self):
        """Test that new adds an object to __objects"""
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.objects)
        self.assertEqual(self.objects[key], obj)

    def test_save(self):
        """Test that save serializes objects to a file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save(obj)
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)
        self.assertEqual(data[key]['__class__'], 'BaseModel')

    def test_reload(self):
        """Test that reload deserializes objects from a file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, self.objects)
        self.assertEqual(self.objects[key].id, obj.id)
        self.assertIsInstance(self.objects[key], BaseModel)

    def test_reload_no_file(self):
        """Test that reload does nothing if no file exists"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}
        self.storage.reload()
        self.assertEqual(self.objects, {})


if __name__ == "__main__":
    unittest.main()
