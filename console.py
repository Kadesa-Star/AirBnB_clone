#!/usr/bin/python3
"""
This is the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter for HBNB"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self, arg):
        # help for the quit command
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        # ensure a new line is printed before exiting
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
