import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_id_is_str(self):
        base = BaseModel()

        self.assertIsInstance(base.id, str)

    def test_init_with_unique_id(self):
        base_1 = BaseModel()
        base_2 = BaseModel()

        self.assertNotEqual(base_1, base_2)
