#!/usr/bin/python3
"""this file for unit testing"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class MaxIntegerTest(unittest.TestCase):
    """test the max int"""

    def test_use(self):
        """test the normal useage"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)

    def test_type(self):
        """Type test"""
        self.assertRaises(TypeError, max_integer, 14)
        self.assertRaises(TypeError, max_integer, ["23", "hello", 12])
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, None)

    def test_empty(self):
        """empty case"""
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_negative(self):
        """negatives test"""
        self.assertEqual(max_integer([-1, -2, 3]), 3)
        self.assertEqual(max_integer([-1, -2, -7]), -1)

    def test_float(self):
        """floats test"""
        self.assertEqual(max_integer([-1.2, -1.1, -7]), -1.1)

    def test_strings(self):
        """strings test"""
        self.assertEqual(max_integer(["hahaha", "xD"]), "xD")
        self.assertEqual(max_integer("UNO"), "U")
