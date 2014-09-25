import unittest

from mathsci.datatypes import Vector
from mathsci.math import chaos

class TestMath(unittest.TestCase):
    def test_chaos_lorenz_attractor(self):
        t = 0.1
        x = 2.3; y = 4.5; z = 6.7
        sigma = 8.9; beta = 0.1; rho = 2.3
        print Vector([sigma * (y - x), x * (rho - z) - y, x * y - beta * z])
        print chaos.lorenz_attractor(t, [x, y, z], sigma=sigma, beta=beta, rho=rho)
        self.assertEqual(chaos.lorenz_attractor(t, [x, y, z], sigma=sigma,
                                                beta=beta, rho=rho),
                         Vector([sigma * (y - x), x * (rho - z) - y,
                          x * y - beta * z]))
if __name__ == '__main__':
    unittest.main()


