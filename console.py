#!/usr/bin/python3

"""Console"""

from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.state import State
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        "comand quit"
        return True

    def do_EOF(self, line):
        "comand eof"
        return True

    def do_create(self, line)
        arguments = line.split()
        if arguments == []:
            print("** class name missing **")
        try:
            

    def do_show(self, line)

    def to_destroy(self, line)
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
