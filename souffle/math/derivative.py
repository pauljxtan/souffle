"""
Evaluating derivatives.
"""
# TODO:
#     Include error estimates for each method?

def forward_difference(f, x, h):
    """
    Evaluates the first derivative at x, with step size h, using a forward
    difference scheme.

    @type  f: function
    @param f: function to differentiate
    @type  x: number
    @param x: position at which to evaluate
    @type  h: number
    @param h: step size

    @rtype: number
    @return: first derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    D = (f(x + h) - f(x)) / h
    return D

def backward_difference(f, x, h):
    """
    Evaluates the first derivative at x, with step size h, using a backward
    difference scheme.

    @type  f: function
    @param f: function to differentiate
    @type  x: number
    @param x: position at which to evaluate
    @type  h: number
    @param h: step size

    @rtype: number
    @return: first derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    D = (f(x) - f(x - h)) / h
    return D

def central_difference(f, x, h):
    """
    Evaluates the first derivative at x, with step size h, using a central
    difference scheme (of degree 1).

    @type  f: function
    @param f: function to differentiate
    @type  x: number
    @param x: position at which to evaluate
    @type  h: number
    @param h: step size

    @rtype: number
    @return: first derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    D = (f(x + h / 2.0) - f(x - h / 2.0)) / h
    return D

# TODO
def central_difference_degree(f, x, h, deg):
    """
    Evaluates the first derivative at x, with step size h, using a central
    difference scheme (of degree deg).

    @type    f: function
    @param   f: function to differentiate
    @type    x: number
    @param   x: position at which to evaluate
    @type    h: number
    @param   h: step size
    @type  deg: number
    @param deg: degree of central difference scheme

    @rtype: number
    @return: first derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    deg = int(deg)
    raise NotImplementedError

def central_difference_second(f, x, h):
    """
    Evaluates the second derivative at x, with step size h, using a central
    difference scheme (of degree 2).

    @type  f: function
    @param f: function to differentiate
    @type  x: number
    @param x: position at which to evaluate
    @type  h: number
    @param h: step size

    @rtype: number
    @return: second derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    D = 2 * (central_difference(f, x + h / 2, h)
             - central_difference(f, x - h / 2, h)) / h
    return D

# TODO
def central_difference_order(f, x, h, n):
    """
    Evaluates the n-th derivative at x, with step size h, using a central
    difference scheme (of degree 1).

    @type  f: function
    @param f: function to differentiate
    @type  x: number
    @param x: position at which to evaluate
    @type  h: number
    @param h: step size
    @type  n: number
    @param n: degree of derivative

    @rtype: number
    @return: n-th derivative of f evaluated at x
    """
    x = float(x)
    h = float(h)
    n = int(n)
    raise NotImplementedError

# TODO
def partial():
    raise NotImplementedError
