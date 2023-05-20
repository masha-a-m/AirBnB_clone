#!/usr/bin/python3
"""Console task."""


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interprete"""

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }


import cmd
import re
from shlex 
import split
from models 
import storage
from models.base_model 
import BaseModel
from models.user 
import User
from models.state 
import State
from models.city 
import City
from models.place 
import Place
from models.amenity import Amenity
from models.review import Review



    def do_all(self, arg):
        """Usage: a."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:

            objl = []
            for obj in storage.all().values():
        
		      if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
