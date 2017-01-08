import unittest

from souffle.utils import frange, same_sign, zeros, ones

class TestUtils(unittest.TestCase):
    def test_frange(self):
        self.assertEqual(frange(0, 5, 11),
                         map(lambda x: float(x) / 2, range(11)))
    def test_samesign(self):
        self.assertTrue(same_sign([1.0, 3.0, 5.0, 7.0, 9.0]))
        self.assertTrue(same_sign([-2.0, -4.0, -6.0, -8.0, -10.0]))
        self.assertFalse(same_sign([1.0, -4.0, 5.0, -8.0, 9.0]))
    def test_zeros(self):
        self.assertEqual(zeros(5), [0.0, 0.0, 0.0, 0.0, 0.0])
    def test_ones(self):
        self.assertEqual(ones(5), [1.0, 1.0, 1.0, 1.0, 1.0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
