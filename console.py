#!/usr/bin/python3
"""
Here's all of the code for the HBNB console
"""

import cmd
from models.base_model import BaseModel
from models.user import User
import models
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def remove_punc(string):
    new_string = ""
    for char in string:
        if char != "," and char != "\"":
            new_string += char
    return new_string


class HBNBCommand(cmd.Cmd):
    """
    Welcome to the console
    """
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
                    result += ", "
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
                            result += ", "
                            result += str(obj)
            except NameError:
                print("** class doesn't exist **")
                return
        result += "]"
        print(result)

    def do_count(self, *args):
        """
        Usage: count [optional class name]
        """
        count = 0
        objects = models.storage.all()
        if not args[0]:
            for obj in objects.values():
                count += 1
        else:
            try:
                _ = eval(args[0])
                for obj in objects.values():
                    class_name = obj.__class__.__name__
                    if class_name == args[0]:
                        count += 1
            except NameError:
                print("** class doesn't exist **")
                return
        print(count)

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

    def default(self, line):
        """
        Method called on an input line when the command is not recognized
        """
        if line[0].isupper():
            fields = line.split(sep=".")
            class_name = fields[0]
            try:
                _ = eval(class_name)
                try:
                    args = fields[1].split("(")
                    command = args[0]
                    method_name = "HBNBCommand().do_" + command
                    obj_id = args[1].strip(")\"'")
                    obj_id = remove_punc(obj_id)
                    if len(obj_id):
                        user_input = "{} {}".format(class_name, obj_id)
                        eval(method_name)(user_input)
                    else:
                        eval(method_name)(class_name)
                except IndexError:
                    super().default(line)
                except AttributeError:
                    print("** invalid command: {} **".format(command))
            except NameError:
                print("** class doesn't exist **")
        else:
            super().default(line)

if __name__ == "__main__":
    HBNBCommand().cmdloop()
