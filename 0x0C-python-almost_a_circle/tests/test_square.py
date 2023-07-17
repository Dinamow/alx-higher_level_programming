#!/usr/bin/python3
"""Test square"""
import unittest
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base
import os
import io
import sys


class test_square(unittest.TestCase):
    """Test for square class"""
    def test_baisc_use(self):
        self.assertIsInstance(Square(10), Base)
        """Test id, width, heigth, x and y"""
        r1 = Square(10)
        r2 = Square(2)
        r3 = Square(10, 0, 0, 12)

        self.assertEqual(r1.id, r2.id - 1)
        self.assertEqual(r3.id, 12)
        self.assertEqual(r1.size, 10)
        self.assertEqual(r2.size, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r2.y, 0)

    def test_size(self):
        """test all cases of width_height"""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1.2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Square(10)
            r.size = -10
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaises(TypeError):
            Square("hello")
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(TypeError):
            Square(10.2)
        with self.assertRaises(TypeError):
            Square(-2.3)

    def test_x_y(self):
        """test all cases of x_y"""
        with self.assertRaises(TypeError):
            r = Square(10)
            r.x = {}
        with self.assertRaises(TypeError):
            r = Square(10, "hello", 1)
        with self.assertRaises(TypeError):
            r = Square(10, True, 1)
        with self.assertRaises(TypeError):
            r = Square(10, {"hello": "meow"}, 1)
        with self.assertRaises(TypeError):
            r = Square(10, 1, "hello")
        with self.assertRaises(TypeError):
            r = Square(10, [1], 2)
        with self.assertRaises(TypeError):
            r = Square(10, {1, 2}, 2)
        with self.assertRaises(TypeError):
            r = Square(10, 2, [2])
        with self.assertRaises(TypeError):
            r = Square(10, 2, {"hello": "meow"})
        with self.assertRaises(TypeError):
            r = Square(10, 2, None)
        with self.assertRaises(TypeError):
            r = Square(10, 1, True)
        with self.assertRaises(TypeError):
            r = Square(10, None, 1)
        with self.assertRaises(TypeError):
            r = Square(10, 2.3, 1)
        with self.assertRaises(TypeError):
            r = Square(10, 3, 1.2)
        r1 = Square(10, 1)
        r2 = Square(10, 1, 2)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r2.y, 2)
        with self.assertRaises(ValueError):
            Square(10, -1, 2)
        rl = Square(10, 0, 2)
        self.assertEqual(rl.x, 0)
        with self.assertRaises(ValueError):
            Square(10, 1, -1)
        rl2 = Square(10, 1, 0)
        self.assertEqual(rl2.y, 0)
        with self.assertRaises(TypeError):
            Square()

    def test_more_than_five_argumnes(self):
        """test using more than 4 arguments"""
        with self.assertRaises(TypeError):
            Square(10, 1, 1, 50, 60)

    def test_x_private(self):
        """test if x is private"""
        with self.assertRaises(AttributeError):
            print(Square(10, 1, 1, 1).__x)

    def test_y_private(self):
        """test if y is private"""
        with self.assertRaises(AttributeError):
            print(Square(10, 1, 1, 1).__y)

    def test_getters_setters(self):
        """test getters and setters"""
        with self.assertRaises(ValueError):
            r = Square(10)
            r.size = -10
        with self.assertRaises(ValueError):
            r = Square(10)
            r.y = -10


class Test_area_square(unittest.TestCase):
    """test_area"""
    def test_area(self):
        r = Square(10)
        self.assertEqual(r.area(), 100)
        r = Square(20)
        self.assertEqual(r.area(), 400)


class Test_display_square(unittest.TestCase):
    """test_display and __str__"""

    @staticmethod
    def what_printed(square, method):
        """function to test __str__ and display"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        if method == "print":
            print(square)
        else:
            square.display()
        sys.stdout = sys.__stdout__
        return capturedOutput

    def test_str(self):
        """test __str__"""
        r1 = Square(4)
        capturedOutput = Test_display_square.what_printed(r1, "print")
        correct = f"[Square] ({r1.id}) 0/0 - 4\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Square(4, 1, 2)
        capturedOutput = Test_display_square.what_printed(r1, "print")
        correct = f"[Square] ({r1.id}) 1/2 - 4\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Square(4, 1)
        capturedOutput = Test_display_square.what_printed(r1, "print")
        correct = f"[Square] ({r1.id}) 1/0 - 4\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Square(4, 0, 1)
        capturedOutput = Test_display_square.what_printed(r1, "print")
        correct = f"[Square] ({r1.id}) 0/1 - 4\n"
        self.assertEqual(correct, capturedOutput.getvalue())

    def test_display(self):
        """test display fun"""
        r1 = Square(3)
        capturedOutput = Test_display_square.what_printed(r1, "Nprint")
        correct = "###\n###\n###\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Square(3, 2)
        capturedOutput = Test_display_square.what_printed(r1, "Nprint")
        correct = "  ###\n  ###\n  ###\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Square(2, 2, 2)
        capturedOutput = Test_display_square.what_printed(r1, "Nprint")
        correct = "\n\n  ##\n  ##\n"
        self.assertEqual(correct, capturedOutput.getvalue())


class Test_to_dict(unittest.TestCase):
    """Test to dictionary"""
    def test_dict(self):
        r1 = Square(3, 0, 0, 1)
        r1_dictionary = r1.to_dictionary()
        test_case = {'id': 1, 'x': 0, 'size': 3, 'y': 0}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Square(5)
        r1 = Square(5)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'id': r1_id, 'x': 0, 'size': 5, 'y': 0}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Square(5)
        r1 = Square(5, 0)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'id': r1_id, 'x': 0, 'size': 5, 'y': 0}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Square(4)
        r1 = Square(4, 1, 2)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'id': r1_id, 'x': 1, 'size': 4, 'y': 2}
        self.assertEqual(test_case, r1_dictionary)


class TestUpdate(unittest.TestCase):
    """Test Update"""
    def test_normal_use(self):
        """normal_use"""
        r = Square(5, 5, 5, 5)
        r.update()
        self.assertEqual('[Square] (5) 5/5 - 5', str(r))
        r = Square(5, 5, 5, 5)
        r.update(10)
        self.assertEqual('[Square] (10) 5/5 - 5', str(r))
        r = Square(5, 5, 5, 5)
        r.update(10, 1, 2)
        self.assertEqual('[Square] (10) 2/5 - 1', str(r))
        r = Square(5, 5, 5, 5)
        r.update(10, 1, 2, 3)
        self.assertEqual('[Square] (10) 2/3 - 1', str(r))
        r = Square(5, 5, 5, 5)
        r.update(10, 1, 2, 3)
        self.assertEqual('[Square] (10) 2/3 - 1', str(r))
        r = Square(5, 5, 5, 5)
        r.update(None)
        self.assertEqual('[Square] (None) 5/5 - 5', str(r))
        r = Square(5, 5, 5, 5)
        r.update(None, 1, 2)
        self.assertEqual('[Square] (None) 2/5 - 1', str(r))
        r = Square(5, 5, 5, 5)
        r.update(10)
        r.update(12)
        self.assertEqual('[Square] (12) 5/5 - 5', str(r))
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello")
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, None)
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, True)
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, 2.3)
        r = Square(5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -1)


class Test_To_Json_String(unittest.TestCase):
    """Test to_json_string"""
    def test_differnt_usages(self):
        """Test"""
        r1 = Square(10, 4, 6, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))
        r1 = Square(10, 6, 4, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertFalse(len(json_dictionary) == 53)
        r1 = Square(10, 4, 6, 1)
        r2 = Square(7, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))
        r1 = Square(10, 4, 6, 1)
        r2 = Square(7, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertFalse(len(json_dictionary) == 106)


class Test_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file"""
    def test_difference(self):
        """test various block of codes"""
        rect = Square(10, 2, 8, 5)
        Square.save_to_file([rect])
        with open("Square.json", "r") as file:
            self.assertFalse(len(file.read()) == 53)
        rect1 = Square(10, 2, 8, 5)
        rect2 = Square(2, 1, 2, 3)
        Square.save_to_file([rect1, rect2])
        with open("Square.json", "r") as file:
            self.assertFalse(len(file.read()) == 105)


class Test_create_in_square(unittest.TestCase):
    """test create with square"""
    def test_square_create(self):
        """test create with square"""
        r1 = Square(3, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)


class Test_load_From_file(unittest.TestCase):
    """test load from file"""
    def test_differnet(self):
        if (os.path.exists("Rectangle.json") is True):
            os.remove("Rectangle.json")
        if (os.path.exists("Square.json") is True):
            os.remove("Square.json")
        if (os.path.exists("Base.json") is True):
            os.remove("Base.json")
        lst = Square.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Square.json")
        lst = Square.load_from_file()
        self.assertEqual(lst, [])
        rect_a = Square(2)
        rect_b = Square(1)
        rect_c = Square(6)
        my_list = [rect_a, rect_b, rect_c]
        Square.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Square.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Square.json")
