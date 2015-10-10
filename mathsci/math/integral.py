"""
Computl.ng integrals.
"""
# TODO:
#     FIX GAUSSIAN QUADRATURE
#     Include error estimates for each method?

# TMP
import numpy as np

import math
import mathsci.utils as utl
import mathsci.datatypes as dtt

def trapezoidal(f, a, b, n):
    """
    Evaluates the integral of f, with endpoints a and b, using the trapezoidal
    rule with n sample points.

    @type  f: function
    @param f: function integrate
    @type  a: number
    @param a: start of interval
    @type  b: number
    @param b: end of interval
    @type  n: number
    @param n: number of sample points

    @rtype: number
    @return: integral of f between a and b
    """
    a = float(a)
    b = float(b)
    n = int(n)

    h = abs(b - a) / n
    s = 0.5 * f(a) + 0.5 * f(b)
    for k in range(1, n):
        s += f(a + k * h)
    I = h * s
    return I

def simpsons(f, a, b, n):
    """
    Evaluates the integral of f, with endpoints a and b, using Simpson's rule
    with n sample points.

    @type  f: function
    @param f: function integrate
    @type  a: number
    @param a: start of interval
    @type  b: number
    @param b: end of interval
    @type  n: number
    @param n: number of sample points

    @rtype: number
    @return: integral of f between a and b
    """
    a = float(a)
    b = float(b)
    n = int(n)

    h = (b - a) / n
    s = f(a) + f(b)
    for k in range(1, n):
        # if k is odd
        if k % 2:
            s += 4.0 * f(a + k * h)
        # if k is even
        else:
            s += 2.0 * f(a + k * h)
    I = 1.0 / 3 * h * s
    return I

# TODO
def adaptive_simpsons():
    return

# TODO
def romberg():
    return

# TODO
def cubic():
    return

# TODO
def quartic():
    return

# TODO
def multiple():
    return
