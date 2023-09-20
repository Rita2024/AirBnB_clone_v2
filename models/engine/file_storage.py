#!/usr/bin/python3
"""This defines a class to manage file storage for hbnb clone"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
	n_dic = {}
        if cls:
            inst_obj = self.__objects
            for key in inst_obj:
                parti = key.replace(".", " ")
                parti = shlex.split(parti)
                if (parti[0] == cls.__name__):
                    n_dic[key] = self.__objects[key]
            return n_dic
        else:
            return self.__objects

def new(self, obj):
        """Adds new object to storage dictionary"""
if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

def save(self):
        """Saves storage dictionary to file"""
json_objects = {}
        for key in self.__objects:
            json_objects[key] = self.__objects[key].to_dict()
with open(self.__file_path, 'w') as f:
            json.dump(json_objects, f)

def reload(self):
        """Loads storage dictionary from file"""
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

def delete(self, obj=None):
        """delete obj from __objects if it’s inside"""
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

def close(self):
        """call reload() method for deserializing the JSON file to objects"""
        self.reload()
