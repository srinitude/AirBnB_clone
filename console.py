#!/usr/bin/python3
"""
Here's all of the code for the HBNB console
"""

import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    Welcome to the console
    """
    intro = "-----------       Welcome to the HBNB console      -----------\n"
    intro += "-----------       Type help to list commands       -----------\n"
    intro += "-----------  Type quit or EOF to exit the program  -----------\n"
    prompt = "(hbnb) "

    # ------- basic HBNB console commands -------
    def do_quit(self, arg):
        """
        Quit console
        """
        return True

    def do_EOF(self, arg):
        """
        Quit console
        """
        return True

    def emptyline(self):
        """
        Overrides empty line to not execute last command
        """
        pass

    def do_create(self, *args):
        """
        Usage: create [class name]
        """
        if not args[0]:
            print("** class name missing **")
            return
        class_name = args[0]
        try:
            instance = eval(class_name)()
            print(instance.id)
        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
