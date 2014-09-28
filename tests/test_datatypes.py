import unittest

from mathsci.datatypes import Vector, Matrix

class TestUtils(unittest.TestCase):
    def test_Vector(self):
        # Addition
        self.assertEqual(Vector([1.0, 2.0, 3.0]) + Vector([4.0, 5.0, 6.0]),
                         Vector([5.0, 7.0, 9.0]))
        # Subtraction
        self.assertEqual(Vector([1.0, 2.0, 3.0]) - Vector([4.0, 5.0, 6.0]),
                         Vector([-3.0, -3.0, -3.0]))

if __name__ == '__main__':
    unittest.main()
