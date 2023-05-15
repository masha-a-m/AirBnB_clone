#!/usr/bin/python3
"""
Custom base class for the entire project.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Custom base for all the classes in the Airbnb console project.
    Arttributes:
        id(str): handles unique user IDs.
        created_at: assign current time of creation.
        updated_at: assign current time of update.
    Method:
        __str__: prints class name, id and an dict presentation
        of all input values.
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

        if not kwargs:
            self.id = str(uuid4)
            self.created_at = self.update_at = datetime.now()
            storage.save()
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ("update_at, created_at"):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)

    def __str__(self):
        """Returns String representation of the class."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                    self.__dict__)

    def save(self):
        """Updates "updated_at" attribute."""
        self.update_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Method returns a dictionary containing the of
        an class and all keys/value of __dict__ instance."""
        objects = __dict__.copy()
        objects["__class__"] = self.__class__.__name__
        for key, value in objects:
            if key in ("update_at", "created_at"):
                v = self.__dict__[key].isoformat()
                objects[key] = v
        return objects
