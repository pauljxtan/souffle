"""
Computing integrals.
"""

# TODO:
#     Include error estimates for each method?

import math
import mathsci.utils
import mathsci.datatypes

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

def adaptive_simpsons():
    return

def romberg():
    return

def cubic():
    return

def quartic():
    return

def gauss_quad(f, a, b, n):
    """
    Integrates a function f using Gaussian quadrature, with endpoints a and b,
    and n sample points.

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
    # Get the sample points and weights
    x, w = gauss_quad_poswei(n)
    x_map, w_map = gauss_map(x, w, a, b)

    I = 0.0
    for i in range(n):
        I += w_map[i] * f(x_map[i])
    
    return I

def gauss_quad_poswei(n):
    """
    Computes the sample points and weights for Gaussian quadrature, for the
    standard interval from -1 to +1, and n sample points.

    @type  n: number
    @param n: number of sample points

    @rtype: vector, vector
    @return: sample points, weights
    """
    # Initial guess for the roots of the Legendre polynomial
    r = mathsci.utils.frange(3, 4*n - 1, n)
    r = mathsci.datatypes.Vector(r)
    r.div_scalar(4*n + 2)
    x = [math.cos(math.pi*a + 1 / (8*n**2 * math.tan(a))) for a in r]
    x = mathsci.datatypes.Vector(x)

    # Use Newton's method to compute the roots
    epsilon = 1.0e9
    # Target accuracy
    delta = 1.0e-9
    dp = mathsci.utils.zeros(n)
    dp = mathsci.datatypes.Vector(dp)
    while abs(epsilon) > delta:
        p0 = mathsci.utils.ones(n)
        p0 = mathsci.datatypes.Vector(p0)
        p1 = mathsci.utils.ones(n)
        p1 = mathsci.datatypes.Vector(p1)
        for i in range(1, n):
            p0, p1 = p1, ((p1 * x).mul_scalar(2*i + 1)
                          - p0.mul_scalar(i)).div_scalar(i + 1)
        dp = (p0 - p1 * x).mul_scalar(n + 1) / ((x*x).sub_scalar(1)).mul_scalar(-1)
        dx = p1 / dp
        x -= dx
        epsilon = max(map(abs, dx))

    # Compute the weights
    # TODO: haven't implemented the exponent magic method for Vector yet, so
    #       hacking this for now
    w = [2 * (n+1)**2 / (n**2 * (1 - x[i]**2) * dp[i]**2) for i in range(n)]
    w = mathsci.datatypes.Vector(w)

    return x, w

def gauss_quad_map(x, w, a, b):
    """
    Maps the sample points onto the specified integration domain with endpoints
    a and b.
    
    @type  x: vector
    @param x: sample points
    @type  w: vector
    @param w: weights
    @type  a: number
    @param a: start of interval
    @type  b: number
    @param b: end of interval

    @rtype: vector, vector
    @return: sample points and weights mapped onto domain
    """
    x_map = x.mul_scalar(0.5 * (b - a)).add_scalar(0.5 * (b + a))
    w_map = w.mul_scalar(0.5 * (b - a))

    return x_map, w_map

def multiple():
    return

if __name__ == "__main__":
    #x, w = gauss_quad_poswei(10)
    #print x.data
    #print w.data
    I = gauss_quad(lambda x: x**2, 2.0, 3.0, 1000)
    print I
