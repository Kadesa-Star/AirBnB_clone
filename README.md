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

# Description of th command line interpreter
	+ This responds to commands
	+ we will use the cmd module, The cmd module makes it easy to make command 
	  line interfaces in your programs.
	+ The module defines only one class: the Cmd class. Creating a command line interpreter 
	  is done by sub-classing the cmd.Cmd class.
	+ The do_xxx method should only take one extra parameter. This parameter corresponds to 
	  the part of the string entered by the user after the command name. The job of do_xxx 
          is to parse this string and to find the command parameter's values.
	+ In the most common case: commands shouldn't return a value.
	+ The exception is when you want to exit the interpreter loop: any command that 
	  returns a true value stops the interpreter.
	## Example
		### The following function defines a command which takes two numerical 
		    arguments and prints the result of the addition:


			def do_add(self,s):
    			l = s.split()
    			if len(l)!=2:
      				 print "*** invalid number of arguments"
       			return
    			try:
      				 l = [int(i) for i in l]
    			except ValueError:
       			print "*** arguments should be numbers"
       			return
    			print l[0]+l[1]

		### Now if you run the interpreter, you will have:


			(Cmd) add 4
			*** invalid number of arguments
			(Cmd) add 5 4
			9

