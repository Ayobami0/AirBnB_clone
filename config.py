from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


ACCEPTED_CLASSES = {
    BaseModel.__name__: BaseModel,
    User.__name__: User,
    Amenity.__name__: Amenity,
    City.__name__: City,
    Place.__name__: Place,
    Review.__name__: Review,
    State.__name__: State
}
