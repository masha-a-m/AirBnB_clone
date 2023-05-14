#!/usr/bin/python3
"""
Custom base class for the entire project.
"""

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """
    Custom base for all the classes in the Airbnb console project.
    Arttributes:
        id(str): handles unique user IDs.
        created_at: assign current time of creation.
        updated_at: assign current time of update.
    Method:
        __str__: prints class name, id and an dict presentationofof all input values.
        save(self): Updates instance attribute "updated_at"
        to_dict(self): returns the dict presentation of an instance.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializing after creation.
        Args:
            *args(self): plane arguments (Note not to be used).
            *Kwargs(self): Keys and value arguments.
        """

        DATE_TIME_FORMAT = '%y-%m-d%T%H:%S.%f'
        if not kwargs:
            self.id = str(uuid4)
            self.created_at = self.update_at = datetime.utcnow()
        else:
            for key, value in kwargs.items():
                if key in ("update_at, created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_TIME_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """Returns String representation of the class."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Updates "updated_at" attribute."""
        self.update_at = datetime.utcnow()
        models.storage.save()
    
    def to_dict(self):
        """Method returns a dictionary containing the of an class and all keys/value of __dict__ instance."""
        objects = {}
        for key, value in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                objects[key] = value.isoformat()
            else:
                objects[key] = value
        objects["__class__"] = self.__class__.__name__
        return objects
