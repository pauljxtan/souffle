"""
Computing integrals.
"""
# TODO:
#     FIX GAUSSIAN QUADRATURE
#     Include error estimates for each method?


import math
import souffle.utils as utl
import souffle.datatypes as dtt

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

def boole(f, a, b):
    """
    Evaluates the integral of f, with endpoints a and b, using Boole's rule.

    @type  f: function
    @param f: function integrate
    @type  a: number
    @param a: start of interval
    @type  b: number
    @param b: end of interval

    @rtype: number
    @return: integral of f between a and b
    """
    x1 = float(a)
    x5 = float(b)

    h = (x5 - x1) / 4
    
    x2 = x1 + h
    x3 = x1 + 2*h
    x4 = x1 + 3*h

    return 2*h / 45 * (7*f(x1) + 32*f(x2) + 12*f(x3) + 32*f(x4) + 7 * f(x5))

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
