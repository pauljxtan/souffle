import unittest

from mathsci.datatypes import Vector
from mathsci.math import chaos, derivative

class TestMath(unittest.TestCase):
    def test_chaos_lorenz_attractor(self):
        t = 0.1
        x = 2.3; y = 4.5; z = 6.7
        sigma = 8.9; beta = 0.1; rho = 2.3
        self.assertEqual(chaos.lorenz_attractor(t, [x, y, z], sigma=sigma,
                                                beta=beta, rho=rho),
                         Vector([sigma * (y - x), x * (rho - z) - y,
                          x * y - beta * z]))

    def test_derivative_difference(self):
        f = lambda x: 2*x**3;
        self.assertTrue(abs(derivative.forward_difference(f, 4, 1e-6) - 96) < 1e-4)
        self.assertTrue(abs(derivative.backward_difference(f, 4, 1e-6) - 96) < 1e-4)
        self.assertTrue(abs(derivative.central_difference(f, 4, 1e-6) - 96) < 1e-4)
        self.assertTrue(abs(derivative.central_difference_second(f, 4, 1e-3) - 96) < 1e-6)


if __name__ == '__main__':
    unittest.main()


