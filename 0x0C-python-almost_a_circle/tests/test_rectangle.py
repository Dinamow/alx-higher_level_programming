#!/usr/bin/python3
"""Test rectangle"""
import unittest
from models.rectangle import Rectangle
from models.base import Base
import os
import io
import sys


class test_rectangle(unittest.TestCase):
    """Test for Rectangle class"""
    def test_baisc_use(self):
        self.assertIsInstance(Rectangle(10, 2), Base)
        """Test id, width, heigth, x and y"""
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.y, 0)

    def test_width_height(self):
        """test all cases of width_height"""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, -2)
        with self.assertRaises(ValueError):
            Rectangle(10, 0)
        with self.assertRaises(TypeError):
            Rectangle("hello", -2)
        with self.assertRaises(TypeError):
            Rectangle(10, "hello")
        with self.assertRaises(TypeError):
            Rectangle(None, -2)
        with self.assertRaises(TypeError):
            Rectangle(2, None)
        with self.assertRaises(TypeError):
            Rectangle(10.2, -2)
        with self.assertRaises(TypeError):
            Rectangle(10, 2.3)
        with self.assertRaises(TypeError):
            Rectangle(10, -2.3)
        with self.assertRaises(TypeError):
            Rectangle(-2.3, 2.3)

    def test_x_y(self):
        """test all cases of x_y"""
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2)
            r.x = {}
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, "hello", 1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, True, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {"hello": "meow"}, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, "hello")
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, [1], 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, {1, 2}, 2)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, [2])
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, {"hello": "meow"})
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 2, None)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 1, True)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, None, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 2.3, 1)
        with self.assertRaises(TypeError):
            r = Rectangle(10, 2, 3, 1.2)
        r1 = Rectangle(10, 23, 1)
        r2 = Rectangle(10, 23, 1, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 23, -1, 2)
        rl = Rectangle(10, 23, 0, 2)
        self.assertEqual(rl.x, 0)
        with self.assertRaises(ValueError):
            Rectangle(10, 23, 1, -1)
        rl2 = Rectangle(10, 23, 1, 0)
        self.assertEqual(rl2.y, 0)
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_more_than_five_argumnes(self):
        """test using more than 5 arguments"""
        with self.assertRaises(TypeError):
            Rectangle(10, 23, 1, 1, 50, 60)

    def test_width_private(self):
        """test if width is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 23, 1, 1, 1).__width)

    def test_height_private(self):
        """test if height is privte"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 23, 1, 1, 1).__height)

    def test_x_private(self):
        """test if x is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 23, 1, 1, 1).__x)

    def test_y_private(self):
        """test if y is private"""
        with self.assertRaises(AttributeError):
            print(Rectangle(10, 23, 1, 1, 1).__y)

    def test_getters_setters(self):
        """test getters and setters"""
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.width = -10
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.height = -10
        with self.assertRaises(ValueError):
            r = Rectangle(10, 2)
            r.y = -10
