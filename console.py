#!/usr/bin/python3

"""Console"""

from ast import arguments
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models import storage
import cmd
import sys

clases = {"State": State, "User": User, "Place": Place, "Review": Review,
          "Amenity": Amenity, "City": City, "BaseModel": BaseModel}

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        "comand quit"
        return True

    def do_EOF(self, line):
        "comand eof"
        return True

    def do_create(self, line):
        arguments = line.split()
        if arguments == []:
            print("** class name missing **")
            return
        elif arguments[0] in clases:
            instance = getattr(sys.modules[__name__], arguments[0])
            inst = instance()
            print(inst.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        arguments = line.split()
        if arguments == []:
            print("** class name missing **")
            return
        if arguments[0] not in clases:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        dic = storage.all()
        key = f"{arguments[0]}.{arguments[1]}"
        if key in dic:
            print(dic[key])
            return

    def do_destroy(self, line):
        arguments = line.split()
        if arguments == []:
            print("** class name missing **")
            return
        if arguments[0] not in clases:
            print("** class doesn't exist **")
            return
        if len(arguments) == 1:
            print("** instance id missing **")
            return
        dic = storage.all()
        key = f"{arguments[0]}.{arguments[1]}"
        if key in dic:
            del(dic[key])
            return

    def do_all(self, line):
        arguments = line.split()
        dic_list = []
        dic = storage.all()
        if arguments == []:
            for key in dic:
                elem = dic[key]
                dic_list.append(str(elem))
            print(dic_list)
            return
        else:
            if arguments[0] in clases:
                for key, value in dic.items():
                    if arguments[0] == value.__class__.__name__:
                        elem = dic[key]
                        dic_list.append(str(elem))
                print(dic_list)
            else:
                print("** class doesn't exist **")
                return
            return

    def do_update(self, line):
        arguments = line.split()
        

if __name__ == '__main__':
    HBNBCommand().cmdloop()