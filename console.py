#!/usr/bin/python3
"""
This is the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """ command interpreter for HBNB"""

    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line + ENTR"""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        # ensure a new line is printed before exiting
        print("")
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
