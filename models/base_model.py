#!/usr/bin/python3
'''contains class BaseModel'''
import uuid
from datetime import datetime
import models

class BaseModel():
    '''class that defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''instantiation of class BaseModel
        args:
            id(str): uuid
            created_at(datetime): current datetime when an instance is created
            updated_at(datetime): updated time when object is changed
        Return: Nothing'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs):
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"] and isinstance(value, str):
                        value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            models.storage.new()

    def __str__(self):
        '''return string representation
        Return: string representation'''
        return f"[{__class__.__name__}] ({self.id}) {self.__dict__}"
    def save(self):
        '''updates the public instance attribute updated_at with the current datetime
        Return: Current datetime'''
        models.storage.save()
        self.updated_at = datetime.now()

    def to_dict(self):
        '''returns a dictionary containing all keys/values of __dict__ of the instance
        Return: dictionary'''
        inst_dict = {**self.__dict__, '__class__': __class__.__name__, 'created_at': self.updated_at.isoformat(), 'updated_at': self.updated_at.isoformat()}
        return inst_dict

    
