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
        x.append(4.0)
        y.append(7.0)
        self.assertEqual(x, Vector([1.0, 2.0, 3.0, 4.0]))
        self.assertEqual(y, Vector([4.0, 5.0, 6.0, 7.0]))

    def test_Matrix(self):
        x = Matrix([[1.0, 2.0, 3.0],
                    [4.0, 5.0, 6.0],
                    [7.0, 8.0, 9.0]])
        y = Matrix([[1.0, 3.0, 2.0],
                    [4.0, 3.0, 5.0],
                    [4.0, 6.0, 5.0]])

        # Element-wise addition
        self.assertEqual(x + y, Matrix([[2.0, 5.0, 5.0],
                                        [8.0, 8.0, 11.0],
                                        [11.0, 14.0, 14.0]]))
        # Element-wise subtraction
        self.assertEqual(x - y, Matrix([[0.0, -1.0, 1.0],
                                        [0.0, 2.0, 1.0],
                                        [3.0, 2.0, 4.0]]))
        # Element-wise multiplication
        self.assertEqual(x * y, Matrix([[1.0, 6.0, 6.0],
                                        [16.0, 15.0, 30.0],
                                        [28.0, 48.0, 45.0]]))

        # Matrix multiplication
        self.assertEqual(x.mul_matrix(y), Matrix([[21.0, 27.0, 27.0],
                                                      [48.0, 63.0, 63.0],
                                                      [75.0, 99.0, 99.0]]))

        # Append row
        x.append_row([1.2, 3.4, 5.6])
        self.assertEqual(x, Matrix([[1.0, 2.0, 3.0],
                                    [4.0, 5.0, 6.0],
                                    [7.0, 8.0, 9.0],
                                    [1.2, 3.4, 5.6]]))
        # Append column
        y.append_col([9.8, 7.6, 5.4])
        self.assertEqual(y, Matrix([[1.0, 3.0, 2.0, 9.8],
                                    [4.0, 3.0, 5.0, 7.6],
                                    [4.0, 6.0, 5.0, 5.4]]))

if __name__ == '__main__':
    unittest.main(verbosity=2)
