#!/usr/bin/python3

"""Console"""
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"

    def do_quit(self, line):
        "comand quit"
        return True

    def do_EOF(self, line):
        "comand eof"
        return True
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
