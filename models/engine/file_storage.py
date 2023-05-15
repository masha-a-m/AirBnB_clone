#!/usr/bin/python3
'''Module file_storage serializes and deserialize JSON types.'''

import json
from models.base_model import BaseModel


class FileStorage:
    '''Custom class for file storage'''
    __file_path = 'file.json'
    __object = {}

    def all(self):
        '''Returns dictionary representation of all objects.'''
        return self.__object

    def new(self, object):
        '''
        Sets in __object with the key <object class name>.id

        Args:
            object(obj): object to write.
        '''
        self.__object[object.__class__.__name__ + "." + object.id] = object

    def save(self):
        '''sets in __objects the object with key <object class name>.id'''
        with open(self.__file_path, 'w+') as f:
            dict_storage = {}
            for k, v in self.__object.item():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage)

    def reload(self):
        '''Deserializes the JSON file to __object.
        Note: works only if file exists
        '''
        try:
            with open(self.__file_path, 'r') as f:
                for value in json.load(f).values():
                    self.new(eval(value["__class__"])(**value))
        except FileNotFoundError:
            return
