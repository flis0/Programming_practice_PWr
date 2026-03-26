# Iwo Chwiszczuk 280043 @iwonieevo

import unittest
import Test_driven_development.solution_2 as pp1

class TestAdd(unittest.TestCase):
    def test_two(self):
        self.assertEqual(pp1.Add("3,4"), 7)
        self.assertEqual(pp1.Add("4.2,2.5"), 6.7)
        self.assertEqual(pp1.Add("5,6"), 11)
        self.assertEqual(pp1.Add("7,8"), 15)
        self.assertEqual(pp1.Add("7,-8"), -1)
        self.assertEqual(pp1.Add("7.1,-8"), -0.9)
        self.assertEqual(pp1.Add("7.1\n-8"), -0.9)
        self.assertEqual(pp1.Add("7.1\n,-8\n"), -0.9)

    def test_one(self):
        self.assertEqual(pp1.Add("4"), 4)
        self.assertEqual(pp1.Add("-3"), -3)
        self.assertEqual(pp1.Add("1.2"), 1.2)
        self.assertEqual(pp1.Add("-3.4"), -3.4)
        self.assertEqual(pp1.Add("-3.4\n"), -3.4)

    def test_empty(self):
        self.assertEqual(pp1.Add(""), 0)
        self.assertEqual(pp1.Add(","), 0)
        self.assertEqual(pp1.Add("\n"), 0)

    def test_type(self):
        self.assertIs(type(pp1.Add("1,1")), int)
        self.assertIs(type(pp1.Add("20000,-7")), int)
        self.assertIs(type(pp1.Add("0.1,2")), float)
        self.assertIs(type(pp1.Add("0.1,-2")), float)

    def test_multiple(self):
        self.assertEqual(pp1.Add("1,1,3,5"), 10)
        self.assertEqual(pp1.Add("-3,1,3,5"), 6)
        self.assertEqual(pp1.Add("-3.5,1,3.2,5"), 5.7)

    def test_error(self):
        self.assertRaises(TypeError, pp1.Add, [1, 2])
        self.assertRaises(ValueError, pp1.Add, "abc")
        self.assertRaises(ValueError, pp1.Add, "?\n\n\n")
        self.assertRaises(ValueError, pp1.Add, "$%")

    def test_newline(self):
        self.assertEqual(pp1.Add("1,1\n3,5"), 10)
        self.assertEqual(pp1.Add("-3,1\n3\n5"), 6)
