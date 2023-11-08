from datetime import datetime
import unittest
from uuid import uuid4

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_is_str(self):
        base = BaseModel()

        self.assertIsInstance(base.id, str)

    def test_init_with_unique_id(self):
        base_1 = BaseModel()
        base_2 = BaseModel()

        self.assertNotEqual(base_1, base_2)

    def test_time_created_is_past(self):
        base_1 = BaseModel()

        self.assertLess(base_1.created_at, datetime.now())

    def test_time_updated_is_created(self):
        base_1 = BaseModel()

        self.assertEqual(base_1.updated_at, base_1.created_at)

    def test_time_updated_on_save(self):
        base_1 = BaseModel()
        prev_up_time = base_1.updated_at

        base_1.save()
        new_up_time = base_1.updated_at

        self.assertNotEqual(prev_up_time, new_up_time)

    def test_base_model_str(self):
        base_1 = BaseModel()

        self.assertEqual(
            base_1.__str__(),
            "[BaseModel] ({}) {}".format(base_1.id, base_1.__dict__),
        )

    def test_base_model_to_dict(self):
        base_1 = BaseModel()
        base_1.save()

        self.assertEqual(
            base_1.to_dict(),
            {
                "id": base_1.id,
                "updated_at": datetime.isoformat(base_1.updated_at),
                "created_at": datetime.isoformat(base_1.created_at),
                "__class__": "BaseModel",
            },
        )

    def test_base_model_from_dict(self):
        base_1 = BaseModel()
        base_1.save()

        base_2 = BaseModel(**base_1.to_dict())

        self.assertEqual(
            base_2.to_dict(),
            {
                "id": base_1.id,
                "updated_at": datetime.isoformat(base_1.updated_at),
                "created_at": datetime.isoformat(base_1.created_at),
                "__class__": "BaseModel",
            },
        )

    def test_base_model_from_dict_is_new(self):
        base_1 = BaseModel()
        base_1.save()

        base_2 = BaseModel(**base_1.to_dict())

        self.assertIsNot(
            base_1,
            base_2
        )

    def test_base_model_from_dict_incomplete_keys(self):
        base_2 = BaseModel(id=uuid4())

        self.assertEqual(
            base_2.to_dict(),
            {
                "id": base_2.id,
                "updated_at": datetime.isoformat(base_2.updated_at),
                "created_at": datetime.isoformat(base_2.created_at),
                "__class__": "BaseModel",
            },
        )
