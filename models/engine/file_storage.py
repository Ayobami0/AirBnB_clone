#!/usr/bin/python3
import json
from importlib import import_module


class FileStorage:
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
            obj (BaseModel): The object to be added.

        Note:
            If 'obj' is not an instance of BaseModel, it is not added
            to the dictionary.
        """
        BaseModel = import_module("models.base_model").BaseModel
        if not isinstance(obj, BaseModel):
            return
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
            with open(self.__file_path, "r", encoding="utf-8") as jf_p:
                objects = json.load(jf_p)
                BaseModel = import_module("models.base_model").BaseModel
                self.__objects = {k: BaseModel(v) for k, v in objects.items()}
        except Exception:
            return
