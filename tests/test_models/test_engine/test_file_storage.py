#!/usr/bin/python3
"""
This are the Test Cases for the file_storage
"""

import unittest
import os
import json
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorageInstantiation(unittest.TestCase):
    """
    This is testing for the instantiation of the file_storage
    """

    def test_FileStorage_instantiation_without_args(self):
        """ this is testing for creation of FileStorage without arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_instantiation_with_args(self):
        # creating a file storage with an argument
        # this should raise a TypeError
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialize(self):
        # is the storage variable in models an instance of FileStorage
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class """

    def setUp(self):
        """
        Set up test environment by creating a temp testfile
        for saving data
        """
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

    def test_new_invalid_object(self):
        """
        Test new raises an error when an invalid object is passed
        """
        with self.assertRaises(AttributeError):
            self.storage.new("invalid_object")

    def test_save(self):
        """Test that save serializes objects to a file"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertIn(key, data)
        self.assertEqual(data[key]['id'], obj.id)
        self.assertEqual(data[key]['__class__'], 'BaseModel')

    def test_save_empty_objects(self):
        """
        test that save correctly handles empty __objects
        """
        FileStorage._FileStorage__objects = {}
        self.storage.save()
        with open(self.file_path, 'r') as file:
            data = json.load(file)
        self.assertEqual(data, {})

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

    def test_reload_corrupted_file(self):
        """
        Test that reload handles a corrupted file gracefully
        """
        with open(self.file_path, 'w') as file:
            file.write("invalid content")
        try:
            self.storage.reload()
        except json.JSONDecodeError:
            self.fail("reload() raided JSONDecodeError unexpectdly")


if __name__ == "__main__":
    unittest.main()
