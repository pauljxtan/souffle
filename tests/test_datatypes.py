import unittest

from mathsci.datatypes import Vector, Matrix

class TestDatatypes(unittest.TestCase):

    def test_Vector(self):
        x = Vector([1.0, 2.0, 3.0])
        y = Vector([4.0, 5.0, 6.0])

        # Element-wise addition
        self.assertEqual(x + y, Vector([5.0, 7.0, 9.0]))
        # Element-wise subtraction
        self.assertEqual(x - y, Vector([-3.0, -3.0, -3.0]))
        # Element-wise multiplication
        self.assertEqual(x * y, Vector([4.0, 10.0, 18.0]))
        # Element-wise division
        self.assertEqual(x / y, Vector([0.25, 0.4, 0.5]))

        # Scalar addition
        self.assertEqual(x.add_scalar(4.0), Vector([5.0, 6.0, 7.0]))
        # Scalar subtraction
        self.assertEqual(x.sub_scalar(4.0), Vector([-3.0, -2.0, -1.0]))
        # Scalar multiplication
        self.assertEqual(x.mul_scalar(4.0), Vector([4.0, 8.0, 12.0]))
        # Scalar division
        self.assertEqual(x.div_scalar(4.0), Vector([0.25, 0.5, 0.75]))

        # Append element
        x.pushback(4.0)
        y.pushback(7.0)
        self.assertEqual(x, Vector([1.0, 2.0, 3.0, 4.0]))
        self.assertEqual(y, Vector([4.0, 5.0, 6.0, 7.0]))

    def test_Matrix(self):
        x = Matrix([[1.0, 2.0, 3.0],
                    [4.0, 5.0, 6.0],
                    [7.0, 8.0, 9.0]])
        y = Matrix([[1.0, 3.0, 2.0],
                    [4.0, 3.0, 5.0],
                    [4.0, 6.0, 5.0]])

        self.assertEqual(x + y, Matrix([[2.0, 5.0, 5.0],
                                        [8.0, 8.0, 11.0],
                                        [11.0, 14.0, 14.0]]))

if __name__ == '__main__':
    unittest.main()
