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


class Test_area_rect(unittest.TestCase):
    """test_area"""
    def test_area(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.area(), 20)
        r = Rectangle(10, 20)
        self.assertEqual(r.area(), 200)


class Test_display_rect(unittest.TestCase):
    """test_display and __str__"""

    @staticmethod
    def what_printed(rectangle, method):
        """function to test __str__ and display"""
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        if method == "print":
            print(rectangle)
        else:
            rectangle.display()
        sys.stdout = sys.__stdout__
        return capturedOutput

    def test_str(self):
        """test __str__"""
        r1 = Rectangle(4, 6)
        capturedOutput = Test_display_rect.what_printed(r1, "print")
        correct = f"[Rectangle] ({r1.id}) 0/0 - 4/6\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Rectangle(4, 6, 1, 2)
        capturedOutput = Test_display_rect.what_printed(r1, "print")
        correct = f"[Rectangle] ({r1.id}) 1/2 - 4/6\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Rectangle(4, 6, 1)
        capturedOutput = Test_display_rect.what_printed(r1, "print")
        correct = f"[Rectangle] ({r1.id}) 1/0 - 4/6\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Rectangle(4, 6, 0, 1)
        capturedOutput = Test_display_rect.what_printed(r1, "print")
        correct = f"[Rectangle] ({r1.id}) 0/1 - 4/6\n"
        self.assertEqual(correct, capturedOutput.getvalue())

    def test_display(self):
        """test display fun"""
        r1 = Rectangle(3, 2)
        capturedOutput = Test_display_rect.what_printed(r1, "Nprint")
        correct = "###\n###\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Rectangle(3, 2, 2)
        capturedOutput = Test_display_rect.what_printed(r1, "Nprint")
        correct = "  ###\n  ###\n"
        self.assertEqual(correct, capturedOutput.getvalue())
        r1 = Rectangle(3, 2, 2, 2)
        capturedOutput = Test_display_rect.what_printed(r1, "Nprint")
        correct = "\n\n  ###\n  ###\n"
        self.assertEqual(correct, capturedOutput.getvalue())


class Test_to_dict(unittest.TestCase):
    """Test to dictionary"""
    def test_dict(self):
        r1 = Rectangle(3, 2, 0, 0, 1)
        r1_dictionary = r1.to_dictionary()
        test_case = {'x': 0, 'y': 0, 'id': 1, 'height': 2, 'width': 3}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Rectangle(5, 4)
        r1 = Rectangle(5, 4)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'x': 0, 'y': 0, 'id': r1_id, 'height': 4, 'width': 5}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Rectangle(5, 4)
        r1 = Rectangle(5, 4, 0)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'x': 0, 'y': 0, 'id': r1_id, 'height': 4, 'width': 5}
        self.assertEqual(test_case, r1_dictionary)
        r2 = Rectangle(5, 4)
        r1 = Rectangle(5, 4, 1, 2)
        r1_dictionary = r1.to_dictionary()
        r1_id = r2.id + 1
        test_case = {'x': 1, 'y': 2, 'id': r1_id, 'height': 4, 'width': 5}
        self.assertEqual(test_case, r1_dictionary)


class TestUpdate(unittest.TestCase):
    """Test Update"""
    def test_normal_use(self):
        """normal_use"""
        r = Rectangle(5, 5, 5, 5, 5)
        r.update()
        self.assertEqual('[Rectangle] (5) 5/5 - 5/5', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(10)
        self.assertEqual('[Rectangle] (10) 5/5 - 5/5', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(10, 1, 2)
        self.assertEqual('[Rectangle] (10) 5/5 - 1/2', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(10, 1, 2, 3)
        self.assertEqual('[Rectangle] (10) 3/5 - 1/2', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(10, 1, 2, 3, 4)
        self.assertEqual('[Rectangle] (10) 3/4 - 1/2', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(None)
        self.assertEqual('[Rectangle] (None) 5/5 - 5/5', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(None, 1, 2)
        self.assertEqual('[Rectangle] (None) 5/5 - 1/2', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        r.update(10)
        r.update(12)
        self.assertEqual('[Rectangle] (12) 5/5 - 5/5', str(r))
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, "hello")
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, None)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, True)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(10, 2.3)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(10, -1)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 2, "height")
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 1, None)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 1, 2.3)
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(10, 1, [2, 1])
        r = Rectangle(5, 5, 5, 5, 5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(10, 1, -2)


class Test_To_Json_String(unittest.TestCase):
    """Test to_json_string"""
    def test_differnt_usages(self):
        """Test"""
        r1 = Rectangle(10, 8, 4, 6, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str, type(json_dictionary))
        r1 = Rectangle(10, 7, 6, 4, 1)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(len(json_dictionary) == 53)
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertEqual(str, type(json_dictionary))
        r1 = Rectangle(10, 7, 4, 6, 1)
        r2 = Rectangle(7, 10, 6, 4, 1)
        dictionaries = [r1.to_dictionary(), r2.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionaries)
        self.assertTrue(len(json_dictionary) == 106)


class Test_save_to_file(unittest.TestCase):
    """Unittests for testing save_to_file"""
    def test_difference(self):
        """test various block of codes"""
        rect = Rectangle(10, 7, 2, 8, 5)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 53)
        rect1 = Rectangle(10, 7, 2, 8, 5)
        rect2 = Rectangle(2, 4, 1, 2, 3)
        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) == 105)


class Test_create_in_rect(unittest.TestCase):
    """test create with rectangle"""
    def test_rect_create(self):
        """test create with rectangle"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
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
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        os.mknod("Rectangle.json")
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])
        rect_a = Rectangle(2, 4)
        rect_b = Rectangle(1, 1)
        rect_c = Rectangle(6, 6)
        my_list = [rect_a, rect_b, rect_c]
        Rectangle.save_to_file([rect_a, rect_b, rect_c])
        my_list_loaded = Rectangle.load_from_file()
        self.assertEqual(type(my_list), type(my_list_loaded))
        self.assertEqual(len(my_list), len(my_list_loaded))
        for i in range(len(my_list)):
            self.assertEqual(type(my_list_loaded[i]), type(my_list[i]))
            self.assertEqual(my_list[i].to_dictionary(),
                             my_list_loaded[i].to_dictionary())
        os.remove("Rectangle.json")
