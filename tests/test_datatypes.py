import unittest

from mathsci.datatypes import Vector, Matrix

class TestUtils(unittest.TestCase):

    def test_Vector(self):
        # Element-wise addition
        self.assertEqual(Vector([1.0, 2.0, 3.0]) + Vector([4.0, 5.0, 6.0]),
                         Vector([5.0, 7.0, 9.0]))
        # Element-wise subtraction
        self.assertEqual(Vector([1.0, 2.0, 3.0]) - Vector([4.0, 5.0, 6.0]),
                         Vector([-3.0, -3.0, -3.0]))
        # Element-wise multiplication
        self.assertEqual(Vector([1.0, 2.0, 3.0]) * Vector([4.0, 5.0, 6.0]),
                         Vector([4.0, 10.0, 18.0]))
        # Element-wise division
        self.assertEqual(Vector([1.0, 2.0, 3.0]) / Vector([4.0, 5.0, 6.0]),
                         Vector([0.25, 0.4, 0.5]))

if __name__ == '__main__':
    unittest.main()
