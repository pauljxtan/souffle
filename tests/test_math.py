import math
import unittest

from souffle.datatypes import Vector, Matrix
from souffle.math import chaos, derivative, discrete, integral, linalg, lineq, maxmin, misc, nonlineq

class TestMath(unittest.TestCase):

    def test_chaos_lorenz_attractor(self):
        t = 0.1
        x = 2.3; y = 4.5; z = 6.7
        sigma = 8.9; beta = 0.1; rho = 2.3

        self.assertEqual(chaos.lorenz_attractor(t, [x, y, z], sigma=sigma,
                                                beta=beta, rho=rho),
                         Vector([sigma * (y - x), x * (rho - z) - y,
                          x * y - beta * z]))

    def test_derivative(self):
        f = lambda x: 2 * x**3
        fp = lambda x: 6 * x**2
        x = 4

        self.assertTrue(abs(derivative.forward_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.backward_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.central_difference(f, x, 1e-6) - fp(x)) < 1e-4)
        self.assertTrue(abs(derivative.central_difference_second(f, x, 1e-3) - fp(x)) < 1e-6)

    def test_discrete(self):
        self.assertEqual(discrete.factorial(7), 5040)
        self.assertEqual(discrete.binomial_coefficient(7, 3), 35)

    def test_integral(self):
        f = lambda x: 9.0 + 8.0*x + 7.0*x**2 + 6.0*x**3
        F = lambda x: 9.0*x + 4.0*x**2 + 7.0/3.0*x**3 + 3.0/2.0*x**4
        a = 0.12
        b = 3.45
        sol = F(b) - F(a)

        self.assertTrue(abs(integral.trapezoidal(f, a, b, 1e5) - sol) < 1e-5)
        self.assertTrue(abs(integral.simpsons(f, a, b, 1e5) - sol) < 1e-5)
        #self.assertTrue(abs(integral.gauss_quad(f, a, b, 1000) - sol) < 1e-5)

    def test_linalg(self):
        A = [1, 3, 2, 4, 3, 5]
        B = [1, 2, 4, 7, 11, 16]
        C = Matrix([[5, 2, 7, 4],
                    [2, 7, 5, 9],
                    [7, 2, 3, 6],
                    [3, 7, 1, 8]])

        self.assertEqual(linalg.dot_product(A, B), 156)
        self.assertEqual(linalg.determinant_minors(C), 488)

    def test_lineq(self):
        A = Matrix([[2.0,  1.0,  4.0,  1.0],
                    [3.0,  4.0, -1.0, -1.0],
                    [1.0, -4.0,  1.0,  5.0],
                    [2.0, -2.0,  1.0,  3.0]])
        b = [-4, 3, 9, 7]
        
        x = lineq.gauss_elim(A, b)
        self.assertTrue(abs(x[0] -  2.0) < 1e-9)
        self.assertTrue(abs(x[1] - -1.0) < 1e-9)
        self.assertTrue(abs(x[2] - -2.0) < 1e-9)
        self.assertTrue(abs(x[3] -  1.0) < 1e-9)

    def test_maxmin(self):
        f1 = lambda x: (x - 3)**2
        f2 = lambda x: -(x - 3)**2

        self.assertTrue(abs(maxmin.golden_ratio_min(f1, -100, 100, 1e-6)[0]
                            - 3) < 1e-7)
        self.assertTrue(abs(maxmin.golden_ratio_max(f2, -100, 100, 1e-6)[0]
                            - 3) < 1e-7)

    def test_misc(self):
        # Compute the so-called "golden ratio" (1/phi) using a continued fraction
        phi = (1.0 + math.sqrt(5.0)) / 2.0
        self.assertTrue(abs(misc.continued_fraction(lambda i: 1.0, lambda i: 1.0, 128) - 1.0 / phi) < 1e-6)

    def test_nonlineq(self):
        f = lambda x: x**2 - 7
        f_deriv = lambda x: 2*x
        x1 = 0.01
        x2 = 5.00
        delta = 1e-6

        self.assertTrue(abs(nonlineq.bisection(f, x1, x2, delta)[0] - math.sqrt(7)) < delta)
        self.assertTrue(abs(nonlineq.newton(f, f_deriv, x1, delta)[0] - math.sqrt(7)) < delta)
        self.assertTrue(abs(nonlineq.secant(f, x1, x2, delta)[0] - math.sqrt(7)) < delta)


if __name__ == '__main__':
    unittest.main(verbosity=2)
