#!/usr/bin/python3
"""The file storage module."""
import json
<<<<<<< HEAD
from importlib import import_module
import models
from models.base_model import BaseModel
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
=======
>>>>>>> 1fb53ec83f4fb381383649fde7fd010fd34af9f5


class FileStorage:
    """Handles the serialization and deserialization of stored models.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Return the dictionary of all objects stored in the __objects attribute.

        Returns:
            dict: A dictionary of all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Add a new object to the __objects dictionary.

        Args:
            obj: The object to be added.

        Note:
            If 'obj' is not an instance of BaseModel, it is not added
            to the dictionary.
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Save objects in the __objects dictionary to a JSON file.
        """
        with open(self.__file_path, "w", encoding="utf-8") as jf_p:
            json.dump(
                {k: obj.to_dict() for k, obj in self.__objects.items()},
                jf_p,
            )

    def reload(self):
        """
        Load objects from the JSON file and populate the __objects dictionary.
        """
        try:
            ACCEPTED_CLASSES = __import__("config").ACCEPTED_CLASSES
            with open(self.__file_path, "r", encoding="utf-8") as jf_p:
                objects = json.load(jf_p)
                self.__objects = {
                    k: ACCEPTED_CLASSES["{}".format(v.get("__class__"))](**v)
                    for k, v in objects.items()
                }
        except Exception:
            return
