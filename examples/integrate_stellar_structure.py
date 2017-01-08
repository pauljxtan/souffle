#!/usr/bin/env python

"""
Integrating the stellar structure equations.

The two coupled equations are:

drho/dr = drho/dP * dP/dr
dM/dr = 4 * pi * r^2 * rho

where

P = (rho / (mu * m_H)) * k_B * T
dP/dr = - ((G * M) / r**2) * rho

We integrate these equations to solve for mass M and density rho, at a given
temperature T.
"""

import math
from matplotlib import pyplot
from souffle.math import odeint
from souffle.physics import astro

# Define constants
mu = 2.0
T = 5.0e2

def main():
    # Set the integration paramters
    f = astro.stellar_structure
    # Space-step
    dr = 1.0e6
    # Starting radius
    r0 = 1.0e6
    # Initial conditions (M, rho)
    X0 = [0.0, 1.0]

    # Integrate it...

    # Using Euler:
    #star = souffle.math.odeint.Euler(f, r0, X0, mu=mu, T=T)
    #star.integrate(dr, 1000, True)
    
    # Using RK4:
    star = odeint.RK4(f, r0, X0, mu=mu, T=T)
    star.integrate(dr, 1000, True)

    # Using Bulirsch-Stoer:
    #star = souffle.math.odeint.BulSto(f, r0, X0, mu=mu, T=T)
    #star.integrate(dr, 1000, 1.0e-6, True)

    # Unpack data
    r = star.t
    M, rho = star.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(r, rho, "x")
    fig1_sp1.set_xlabel("Distance from center [m]")
    fig1_sp1.set_ylabel("Density [kg m^{-3}]")

    pyplot.show()

if __name__ == "__main__":
    main()
