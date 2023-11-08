import uuid
import datetime


class BaseModel:
    def __init__(self) -> None:
        """
        Initialize a BaseModel instance with unique identifier and timestamps.

        Attributes:
            id (str): A unique identifier generated using uuid4.
            created_at (datetime.datetime): Timestamp representing
                the creation time.
            updated_at (datetime.datetime): Timestamp representing
                the last update time.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

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
            **{k: self.__dict__[k] for k in self.__dict__
                if k not in ["created_at", "updated_at"]},
            "created_at": datetime.datetime.isoformat(self.created_at),
            "updated_at": datetime.datetime.isoformat(self.updated_at),
            "__class__": self.__class__.__name__
        }
