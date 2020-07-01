#!/usr/bin/python3
"""
    TestFileStorage module
"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):

    @classmethod
    def create_instance(cls):
        """create instance for the test"""
        cls.data1 = FileStorage()
        cls.data2 = storage.all()

    def test_isinstance_FileStorage(self):
        """test if the data is an type FileStorage"""

        self.assertTrue(isinstance(self.data1, FileStorage))
        self.assertTrue(isinstance(self.data2, FileStorage))


if __name__ == '__main__':
    unittest.main()
