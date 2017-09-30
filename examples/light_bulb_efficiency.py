#!/usr/bin/env python

"""
Investigating the efficiency of a light bulb.
"""

import math
from matplotlib import pyplot
from souffle import constants
from souffle import utils
from souffle.math import integral, maxmin

# Endpoints for visible wavelengths [m]
LAM1 = 3.9e-7
LAM2 = 7.5e-7

def efficiency_integrand(x):
    """
    The integrand in the efficiency equation.
    """
    return x**3 / (math.exp(x) - 1)

def efficiency(T):
    """
    The efficiency of a light bulb, i.e. the fraction of radiation energy
    falling in the visible wavelengths.
    """
    C = 15.0 / math.pi**4
    # Compute integral endpoints
    a = (constants.h * constants.c / (LAM2 * constants.k_B * T))
    b = (constants.h * constants.c / (LAM1 * constants.k_B * T))
    # Use Gaussian quadrature with 100 sample points to evaluate the integral
    #I = integral.gauss_quad(efficiency_integrad, a, b, 100)
    # Use Simpson's rule to evaluate the integral with 100 sample points
    I = integral.simpsons(efficiency_integrand, a, b, 100)
    return C * I

def main():
    # Find temperature of maximum efficiency using a golden ratio search
    x1 = 3000.0
    x4 = 10000.0

    T_maxeff, n_iter = maxmin.golden_ratio_max(efficiency, x1, x4, 1.0e-6)
    print("Temperature of maximum efficiency = %.6f K (%d iterations)"
          % (T_maxeff, n_iter))

    # Plot the efficiency to check our value
    print("Plotting efficiency...")
    temps = utils.frange(100.0, 10000.0, 1000)
    efficiencies = [efficiency(temp) for temp in temps]

    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.set_title("Efficiency of a light bulb")
    fig1_sp1.set_xlabel("Temperature [K]")
    fig1_sp1.set_ylabel("Efficiency")
    fig1_sp1.set_xlim(100.0, 10000.0)
    fig1_sp1.set_ylim(0.0, 0.5)
    fig1_sp1.plot(temps, efficiencies, "-")
    fig1_sp1.scatter(T_maxeff, efficiency(T_maxeff))
    pyplot.show()

if __name__ == "__main__":
    main()

