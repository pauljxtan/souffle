#!/usr/bin/env python

"""
Integrating the Lorenz attractor.
"""

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from mathsci.math import chaos, odeint

def main():
    # Set integration function
    f = chaos.lorenz_attractor
    # Length of timestep
    dt = 0.01
    # Initial time
    t0 = 0.0
    # Initial coordinates
    X0 = [0.01, 0.01, 0.01]
    # Integration constants
    sigma = 10.0
    beta = 8.0 / 3.0
    rho = 28.0

    # Integrate it...

    # Using Euler:
    #lorenz = odeint.Euler(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    #lorenz.integrate(dt, 10000, True)
    
    # Using RK4:
    #lorenz = odeint.RK4(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    #lorenz.integrate(dt, 10000, True)

    # Using Bulirsch-Stoer:
    lorenz = odeint.BulSto(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    lorenz.integrate(dt, 10000, 1.0e-6, True)

    # Unpack data
    t = lorenz.t
    x, y, z = lorenz.unpack()

    # Plot time series
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, x, label="x")
    fig1_sp1.plot(t, y, label="y")
    fig1_sp1.plot(t, z, label="z")
    fig1_sp1.legend()

    # Plot in 3D
    fig2 = pyplot.figure()
    fig2.sp1 = fig2.add_subplot(111, projection="3d")
    fig2.sp1.plot(x, y, z)

    pyplot.show()

if __name__ == "__main__":
    main()
