#!/usr/bin/python3
"""
Here's all of the code for the HBNB console
"""

import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
    """
    Welcome to the console
    """
    intro = "-----------       Welcome to the HBNB console      -----------\n"
    intro += "-----------       Type help to list commands       -----------\n"
    intro += "-----------  Type quit or EOF to exit the program  -----------\n"
    prompt = "(hbnb) "

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
            return

    def do_show(self, *args):
        """
        Usage: show [class name] [id]
        """
        if not args[0]:
            print("** class name missing **")
            return
        try:
            fields = args[0].split(sep=" ")
            class_name = fields[0]
            _ = eval(class_name)
            class_id = fields[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        for obj in objects.values():
            if class_name == obj.__class__.__name__ and class_id == obj.id:
                print(obj)
                return
        print("** no instance found **")

    def do_destroy(self, *args):
        """
        Usage: destroy [class name] [id]
        """
        if not args[0]:
            print("** class name missing **")
            return
        try:
            fields = args[0].split(sep=" ")
            class_name = fields[0]
            _ = eval(class_name)
            class_id = fields[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        for key, obj in objects.items():
            if class_name == obj.__class__.__name__ and class_id == obj.id:
                del objects[key]
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self, *args):
        """
        Usage: all [optional class name]
        """
        result = "["
        first = True
        objects = models.storage.all()
        if not args[0]:
            for obj in objects.values():
                if first:
                    result += str(obj)
                    first = False
                else:
                    result += ","
                    result += "\n"
                    result += str(obj)
        else:
            try:
                _ = eval(args[0])
                for obj in objects.values():
                    class_name = obj.__class__.__name__
                    if class_name == args[0]:
                        if first:
                            result += str(obj)
                            first = False
                        else:
                            result += ","
                            result += "\n"
                            result += str(obj)
            except NameError:
                print("** class doesn't exist **")
                return
        result += "]"
        print(result)

    def do_update(self, *args):
        """
        Usage: update [class name] [id] [attribute name] "[attribute value]"
        """
        if not args[0]:
            print("** class name missing **")
            return
        try:
            fields = args[0].split(sep=" ")
            class_name = fields[0]
            _ = eval(class_name)
            class_id = fields[1]
        except NameError:
            print("** class doesn't exist **")
            return
        except IndexError:
            print("** instance id missing **")
            return
        objects = models.storage.all()
        for obj in objects.values():
            if obj.id == class_id:
                try:
                    name = fields[2]
                    try:
                        val = fields[3]
                        val = val.strip("\"'")
                        setattr(obj, name, str(val))
                        models.storage.save()
                        return
                    except IndexError:
                        print("** value missing **")
                        return
                except IndexError:
                    print("** attribute name missing **")
                    return
        print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
