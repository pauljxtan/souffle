#!/usr/bin/env python

"""
Computing various trigonometric functions by solving nonlinear equations.
"""

import math
from souffle.math import nonlineq

def arctanh(x):
    """
    Computes the inverse hyperbolic tangent using Newton's method.
    """
    f = lambda y: math.tanh(y) - x
    f_deriv = lambda y: math.cosh(y)**(-2)
    x, n_iter = nonlineq.newton(f, f_deriv, 0.0, 1e-12)

    return x

if __name__ == "__main__":
    print("arctanh(0.5) =", arctanh(0.5))

