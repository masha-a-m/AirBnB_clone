#!/usr/bin/python3

from datetime import datetime  # Importing the datetime module
from uuid import uuid4  # Importing the uuid4 function from the uuid module


class BaseModel:
    """
    A base model class that provides common functionality for other models.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor method for BaseModel.

        Initializes the object with provided
        attributes or generates default values.
        """
        if not kwargs:
            # If no keyword arguments are provided, generate default values
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
        else:
            # If keyword arguments are provided,
            # set the corresponding attributes
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ("created_at", "updated_at"):
                        # If the attribute is a timestamp, convert
                        # it from ISO format to datetime object
                        setattr(self, k, datetime.fromisoformat(v))
                    else:
                        # Set the attribute with the provided value
                        setattr(self, k, v)

    def __str__(self) -> str:
        """
        Return a string representation of the object.

        Returns:
            str: A formatted string containing the class name,
            id, and attribute dictionary.
        """
        return "[{}] ({}) {}".format(__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Update the 'updated_at' attribute with the current timestamp.
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Convert the object to a dictionary representation.

        Returns:
            dict: A dictionary containing the
            object's attributes and class name.
        """
        obj = self.__dict__.copy()
        obj["__class__"] = __class__.__name__

        for k, v in obj.items():
            if k in ("created_at", "updated_at"):
                obj[k] = datetime.isoformat(v)

        return obj
