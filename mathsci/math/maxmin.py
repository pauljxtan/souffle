"""
Finding the maxima and minima of functions.
"""
import math
from mathsci.constants import GOLDEN_RATIO

def golden_ratio_min(f, x1, x4, delta, n_iter=0):
    """
    Recursively computes a local minimum of a function f, given an initial
    search bracket (x1, x4).
    
    @type       f: function
    @type      x1: number
    @param     x1: start of initial search bracket
    @type      x4: number
    @param     x4: end of initial search bracket
    @type   delta: number
    @param  delta: desired accuracy
    @type  n_iter: number
    @param n_iter: iteration counter
        
    @rtype: number, number
    @return: final value, iteration counter
    """
    # Compute x2 and x3 from x1 and x4 according to the golden ratio rule
    x3 = x1 + (1 / GOLDEN_RATIO) * (x4 - x1)
    x1_x4_mid = (x1 + x4) / 2
    x2 = x1_x4_mid - (x3 - x1_x4_mid)

    # Evaluate the function at each point
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)

    # Check that at least one of f(x2), f(x3) is less than both f(x1) and f(x4)
    #if not ((f2 < f1 and f2 < f4) or (f3 < f1 and f3 < f4)):
    #    raise ValueError("Neither f(x2) nor f(x3) is less than both f(x1) "\
    #                     "and f(x4)")

    # If f(x2) < f(x3), x3 becomes x4, x2 becomes x3
    if f2 < f3:
        x4 = x3
        x3 = x2
        # Compute the new x2
        x1_x4_mid = (x1 + x4) / 2
        x2 = x1_x4_mid - (x3 - x1_x4_mid)
        # Evaluate the function at the new x2
        f2 = f(x2)
    # If f(x2) > f(x3), x2 becomes x1, x3 becomes x2
    else:
        x1 = x2
        x2 = x3
        # Compute the new x3
        x3 = x1 + (1 / GOLDEN_RATIO) * (x4 - x1)
        # Evaluate the function at the new x3
        f3 = f(x3)

    n_iter += 1

    # If we have reached the desired accuracy, return the midpoint of x2 and x3
    if abs(x4 - x1) < delta:
        x_mid = (x2 + x3) / 2
        return x_mid, n_iter
    # Otherwise, repeat procedure
    else:
        return golden_ratio_min(f, x1, x4, delta, n_iter)

def golden_ratio_max(f, x1, x4, delta, n_iter=0):
    """
    Recursively computes a local maximum of a function f, given an initial
    search bracket (x1, x4).
    
    @type       f: function
    @type      x1: number
    @param     x1: start of initial search bracket
    @type      x4: number
    @param     x4: end of initial search bracket
    @type   delta: number
    @param  delta: desired accuracy
    @type  n_iter: number
    @param n_iter: iteration counter
        
    @rtype: number, number
    @return: final value, iteration counter
    """
    # Compute x2 and x3 from x1 and x4 according to the golden ratio rule
    x3 = x1 + (1 / GOLDEN_RATIO) * (x4 - x1)
    x1_x4_mid = (x1 + x4) / 2
    x2 = x1_x4_mid - (x3 - x1_x4_mid)

    # Evaluate the function at each point
    f1 = -f(x1)
    f2 = -f(x2)
    f3 = -f(x3)
    f4 = -f(x4)

    # Check that at least one of -f(x2), -f(x3) is less than
    # both -f(x1) and -f(x4)
    #if not ((f2 < f1 and f2 < f4) or (f3 < f1 and f3 < f4)):
    #    raise ValueError("Neither -f(x2) nor -f(x3) is less than both -f(x1) "\
    #                     "and -f(x4)")

    # If -f(x2) < -f(x3), x3 becomes x4, x2 becomes x3
    if f2 < f3:
        x4 = x3
        x3 = x2
        # Compute the new x2
        x1_x4_mid = (x1 + x4) / 2
        x2 = x1_x4_mid - (x3 - x1_x4_mid)
        # Evaluate the function at the new x2
        f2 = -f(x2)
    # If f(x2) > f(x3), x2 becomes x1, x3 becomes x2
    else:
        x1 = x2
        x2 = x3
        # Compute the new x3
        x3 = x1 + (1 / GOLDEN_RATIO) * (x4 - x1)
        # Evaluate the function at the new x3
        f3 = -f(x3)

    n_iter += 1

    # If we have reached the desired accuracy, return the midpoint of x2 and x3
    if abs(x4 - x1) < delta:
        x_mid = (x2 + x3) / 2
        return x_mid, n_iter
    # Otherwise, repeat procedure
    else:
        return golden_ratio_max(f, x1, x4, delta, n_iter)
