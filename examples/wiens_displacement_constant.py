#!/usr/bin/env python

"""
Computing Wien's displacement constant using various nonlinear equation-solving
methods, and estimating the surface temperature of the Sun.
"""

import math
from souffle import constants
from souffle.math import nonlineq

def wien(x):
    """
    Wien's displacement constant is defined by b = h * c / (k_B * x), where
    x is described by this nonlinear equation.
    """
    return 5 * math.exp(-x) + x - 5

def wien_deriv(x):
    """
    The first derivative of the nonlinear equation in wien().
    """
    return 1 - 5 * math.exp(-x)

def main():
    # Solve for x using ...
    # ... the bisection method:
    x_bisect, n_iter_bisect = nonlineq.bisection(wien, 2.0, 8.0, 1.0e-6)
    # ... Newton's method:
    x_newton, n_iter_newton = nonlineq.newton(wien, wien_deriv, 2.0, 1.0e-6)
    # ... the secant method:
    x_secant, n_iter_secant = nonlineq.secant(wien, 2.0, 3.0, 1.0e-6)
    
    # Solve for Wien's displacement constant
    b_bisect = constants.h * constants.c / (constants.k_B * x_bisect)
    b_newton = constants.h * constants.c / (constants.k_B * x_newton)
    b_secant = constants.h * constants.c / (constants.k_B * x_secant)

    print ("Bisection method:\t%.7f x 10^3 m K (%d iterations)"
           % (b_bisect * 1e3, n_iter_bisect))
    print ("Newton's method:\t%.7f x 10^3 m K (%d iterations)"
           % (b_newton * 1e3, n_iter_newton))
    print ("Secant method:\t\t%.7f x 10^3 m K (%d iterations)"
           % (b_secant * 1e3, n_iter_secant))
    print
    
    # Peak wavelength in solar radiation [m]
    wl_peak_sol = 5.02e-7
    
    # Estimate the surface temperature of the Sun
    T_sol = b_secant / wl_peak_sol
    print "Estimated surface temperature of sun = %.2f K" % T_sol

if __name__ == "__main__":
    main()
