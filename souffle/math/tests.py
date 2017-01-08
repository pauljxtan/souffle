import unittest
from souffle.math import derivative, integral

class DerivativeTests(unittest.TestCase):

    def test_forward_difference(self):
        f = lambda x: 1.2 * x**3.4
        x = 5.6
        h = 1e-5
        self.assertTrue(abs(derivative.forward_difference(f, x, h) - 254.866) < 1e-3)

    def test_backward_difference(self):
        f = lambda x: 1.3 * x**2.4
        x = 3.5
        h = 1e-4
        self.assertTrue(abs(derivative.backward_difference(f, x, h) - 18.024) < 1e-3)

class IntegralTests(unittest.TestCase):

    def test_trapezoidal(self):
        f = lambda x: 1.2 * x**3.4
        a = 2.3
        b = 4.5
        n = 1e4
        self.assertTrue(abs(integral.trapezoidal(f, a, b, n) - 193.460148) < 1e-6)

    def test_simpsons(self):
        f = lambda x: 2.3 * x**4.5
        a = 3.4
        b = 5.6
        n = 1e2
        self.assertTrue(abs(integral.simpsons(f, a, b, n) - 5099.687412) < 1e-6)

    def test_boole(self):
        f = lambda x: 3.4 * x**5.6
        a = 4.5
        b = 6.7
        n = 1e3
        self.assertTrue(abs(integral.simpsons(f, a, b, n) - 135343.850360) < 1e-6)

TEST_CASES = (DerivativeTests, IntegralTests, )

def suite():
    return unittest.TestSuite(
        [unittest.TestLoader().loadTestsFromTestCase(test_case)
        for test_case in TEST_CASES]
    )

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
