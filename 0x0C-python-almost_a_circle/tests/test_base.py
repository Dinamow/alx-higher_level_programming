#!/usr/bin/python3
"""Unittest for Base"""
import unittest
from models.base import Base


class Test_ID(unittest.TestCase):
    """test for Base"""
    def test_create_id(self):
        """test id's values"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base(1.4)
        b6 = Base(-2)
        b7 = Base(0)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 1.4)
        self.assertEqual(b6.id, -2)
        self.assertEqual(b7.id, 0)

    def test_non_int_id(self):
        """Test non int Id"""
        b1 = Base("Hello")
        b2 = Base(-2.3)
        b3 = Base([1, 2, 3])
        b4 = Base({"hello": 1})
        b5 = Base((1, 2))
        b6 = Base({1, 2})
        b7 = Base(True)

        self.assertEqual(b1.id, "Hello")
        self.assertEqual(b2.id, -2.3)
        self.assertEqual(b3.id, [1, 2, 3])
        self.assertEqual(b4.id, {"hello": 1})
        self.assertEqual(b5.id, (1, 2))
        self.assertEqual(b6.id, {1, 2})
        self.assertEqual(b7.id, True)

    def test_increment_id(self):
        """test increment id"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base(5)
        self.assertEqual(b2.id, 5)
        b3 = Base(None)
        self.assertEqual(b3.id, 2)

    def test_id_errors(self):
        """test_id_errors"""
        with self.assertRaises(TypeError):
            Base(None, 3)
        with self.assertRaises(TypeError):
            Base(1, None)

    def test_to_json_string_base(self):
        """test_to_json_string"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, "[]")

        json_string = Base.to_json_string([])
        self.assertEqual(json_string, "[]")

        with self.assertRaises(TypeError):
            json_string = Base.to_json_string([], "hello")

        with self.assertRaises(TypeError):
            json_string = Base.to_json_string()
