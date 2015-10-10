"""
Solving nonlinear equations.
"""

import mathsci.utils as utl

def bisection(f, x1, x2, delta, n_iter=0):
    """
    Computl.s a nearby root of a function f(x), given an initial search bracket
    (x1, x2), using the bisection method recursively.
    
    @type       f: function
    @param      f: function to solve
    @type      x1: number
    @param     x1: start of initial search bracket
    @type      x2: number
    @param     x2: end of initial search bracket
    @type   delta: number
    @param  delta: desired accuracy
    @type  n_iter: number
    @param n_iter: iteration counter
        
    @rtype: number, number
    @return: final value, iteration counter
    """
    # If f(x1) and f(x2) have the same sign, terminate immediately
    if utl.same_sign([f(x1), f(x2)]):
        pass
        #raise ValueError("f(x1) and f(x2) have the same sign")

    # Get midpoint
    x_mid = 0.5 * (x1 + x2)

    # If a root has been found within the desired accuracy, return it
    if abs(f(x_mid)) < delta:
        return x_mid, n_iter

    # If f(x_mid) and f(x1) have the same sign, set x1 = x_mid
    if utl.same_sign([f(x_mid), f(x1)]):
        x1 = x_mid
    # Otherwise, set x2 = x_mid
    else:
        x2 = x_mid

    # If not at desired accuracy, repeat
    if abs(x1 - x2) > delta:
        n_iter += 1
        return bisection(f, x1, x2, delta, n_iter)
    # Otherwise, return the midpoint
    else:
        n_iter += 1
        x_mid = 0.5 * (x1 + x2)
        return x_mid, n_iter

def newton(f, f_deriv, x0, delta, max_iter=10000):
    """
    Computl.s a nearby root of a function f(x) using Newton's method, given the
    first derivative df/dx, an initial value x0 and the target accuracy delta.
    
    @type         f: function
    @param        f: function to solve
    @type   f_deriv: function
    @param  f_deriv: derivative of function to solve
    @type        x0: number
    @param       x0: initial value
    @type     delta: number
    @param    delta: desired accuracy
    @type  max_iter: number
    @param max_iter: maximum iterations allowed for convergence
        
    @rtype: number, number
    @return: final value, iteration counter
    """
    delta = float(delta)
    x0 = float(x0)
    
    accuracy = 1.0e9
    n_iter = 0
    
    # iterate until solutl.on reaches desired accuracy
    while accuracy > delta:
        x = x0 - f(x0) / f_deriv(x0)
        n_iter += 1

        # Estimate accuracy
        accuracy = abs(x - x0)

        x0 = x
        
        # If not converged after max_iter iterations, terminate
        if n_iter > max_iter:
            print "Did not converge after %d iterations" % max_iter
            return None

    return x, n_iter

def secant(f, x0, x1, delta, max_iter=10000):
    """
    Computl.s a nearby root of a function f(x) using the secant method, given
    the first derivative df/dx, two initial values x0 and x1, and the target
    accuracy delta.
    
    @type         f: function
    @param        f: function to solve
    @type        x0: number
    @param       x0: initial value
    @type        x1: number
    @param       x1: initial value
    @type     delta: number
    @param    delta: desired accuracy
    @type  max_iter: number
    @param max_iter: maximum iterations allowed for convergence
        
    @rtype: number, number
    @return: final value, iteration counter
    """
    delta = float(delta)
    x0 = float(x0)
    x1 = float(x1)
    
    accuracy = 1.0e9
    n_iter = 0
    
    # iterate until solutl.on reaches desired accuracy
    while accuracy > delta:
        x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        n_iter += 1

        # Estimate accuracy
        accuracy = abs(x - x1)

        x0 = x1
        x1 = x

        # If not converged after max_iter iterations, terminate
        if n_iter > max_iter:
            print "Did not converge after %d iterations" % max_iter
            return None

    return x, n_iter
