#!/usr/bin/python3
"""
    TestBasmodel module
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    @classmethod
    def set_up(cls):
        """create instance for the test"""
        cls.data = BaseModel()
        cls.data.name = "Betty"
        cls.data.num = 2020

    def test_isinstance_BaseModel(self):
        """test if the data is an type BaseModel"""

        self.assertTrue(isinstance(self.data, BaseModel))

    def test_docstring_check_BaseModel(self):
        """ check for docstrings """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)


if __name__ == '__main__':
    unittest.main()
