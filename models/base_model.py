#!/usr/bin/python3
import uuid
import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs) -> None:
        """
        Initialize a BaseModel instance with unique identifier and timestamps.

        Attributes:
            id (str): A unique identifier generated using uuid4.
            created_at (datetime.datetime): Timestamp representing
                the creation time.
            updated_at (datetime.datetime): Timestamp representing
                the last update time.
        """
        if args and len(args) != 0:
            pass
        if kwargs and len(kwargs) != 0:
            # this for loop is mainly to cater for cases where insurficient
            # parameters was provided in the dict. Only the id, created_at,
            # and updated_at attributes are set. It can be removed later on.
            for k in ["created_at", "updated_at", "id"]:
                if k not in kwargs.keys():
                    if k == "id":
                        setattr(self, k, str(uuid.uuid4()))
                    else:
                        setattr(self, k, datetime.datetime.now())
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
            return
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)

    def __str__(self) -> str:
        """
        Return a string representation of the BaseModel instance.

        Returns:
            str: A string containing class name, id, and attributes dictionary.

        Example:
            >>> model = BaseModel()
            >>> str(model)
            '[BaseModel] (unique_id) {"id": "unique_id",
            "created_at": timestamp, "updated_at": timestamp}'
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__,
        )

    def save(self):
        """
        Update the 'updated_at' timestamp to the current time.
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Convert the BaseModel instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance's
                attributes and metadata.

        Example:
            >>> model = BaseModel()
            >>> model.to_dict()
            {
                'id': 'unique_id',
                'created_at': 'timestamp',
                'updated_at': 'timestamp',
                '__class__': 'BaseModel'
            }
        """
        return {
            **{
                k: self.__dict__[k]
                for k in self.__dict__
                if k not in ["created_at", "updated_at"]
            },
            "created_at": datetime.datetime.isoformat(self.created_at),
            "updated_at": datetime.datetime.isoformat(self.updated_at),
            "__class__": self.__class__.__name__,
        }
