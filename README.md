# THE AIRBNB CLONE PROJECT

This is a clone of the AirBnB Website.

## The Project has several parts
## These include
+ The Console
	### this is the entry point of our command interpreter 
	+ here you create your data model
	+ Manage the objects via a console i.e
		+ Create
		+ Read 
		+ Update 
		+ Destroy
	+ we also incorporate JSON data interchange in file storage

+ Base Model and Inheritance
	### this is the class from which all other classes
	### will inherit from
+ Python unique identifier (UUID)
	+ here we will incorporate the Universal Unique 
	+ identifier to create unique id's for users
	+ will help in differentiating between the instances of a class
+ Unittest
	## we create test cases using the Unittest 

# models directory will contain all classes used for the entire project. 
	## A class, called “model” in a OOP project is the representation of an object/instance.
	## tests directory will contain all unit tests.
	## console.py file is the entry point of our command interpreter.
	## models/base_model.py file is the base class of all our models. It contains common elements:
	## attributes: id, created_at and updated_at
	## methods: save() and to_json()
	## models/engine directory will contain all storage classes (using the same prototype). 
	## For the moment you will have only one: file_storage.py

