#!/usr/bin/python3
'''class FileStorage'''
import json
from models.base_model import BaseModel

class FileStorage():
    '''serializes instances to a JSON file and deserializes JSON file to instances'''

    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''method that returns the dictionary objects
        Return: objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key
        args:
            obj(any): an object
        Return: Nothing'''
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        '''serializes __objects to the JSON file 
        Return: Nothing'''
        object_dict = {obj : FileStorage.__objects[obj].to_dict() for obj in FileStorage.__objects.keys()}
        with open(FileStorage.__file_path, 'w') as my_file:
            json.dump(object_dict, my_file)

    def reload(self):
        '''deserializes the JSON file to __objects
        Return: Nothing'''
        try:
            with open(FileStorage.__file_path) as my_file:
                dict_obj = json.load(my_file)
                for obj in dict_obj.values():
                    class_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(class_name)(**obj))
        except FileNotFoundError:
            return
    
        
