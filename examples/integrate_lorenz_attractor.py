#!/usr/bin/env python

"""
Integrating the Lorenz attractor.
"""

import matplotlib.pyplot as pyplot
from mpl_toolkits.mplot3d import Axes3D
import mathsci.math.chaos
import mathsci.math.odeint

def main():
    # Set the integration paramters
    f = mathsci.math.chaos.lorenz_attractor
    dt = 0.01
    t0 = 0.0
    X0 = [0.01, 0.01, 0.01]
    sigma = 10.0
    beta = 8.0 / 3.0
    rho = 28.0

    # Integrate it...

    # Using Euler:
    #euler_lorenz = mathsci.math.odeint.Euler(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    #euler_lorenz.integrate(dt, 10000, True)
    
    # Using RK4:
    #rk4_lorenz = mathsci.math.odeint.RK4(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    #rk4_lorenz.integrate(dt, 10000, True)

    # Using Bulirsch-Stoer:
    bulsto_lorenz = mathsci.math.odeint.BulSto(f, t0, X0, sigma=sigma, beta=beta, rho=rho)
    bulsto_lorenz.integrate(dt, 10000, 1.0e-6, True)

    # Unpack data
    #t = euler_lorenz.t
    #x, y, z = euler_lorenz.unpack()
    #t = rk4_lorenz.t
    #x, y, z = rk4_lorenz.unpack()
    t = bulsto_lorenz.t
    x, y, z = bulsto_lorenz.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, x, label="x")
    fig1_sp1.plot(t, y, label="y")
    fig1_sp1.plot(t, z, label="z")
    fig1_sp1.legend()

    fig2 = pyplot.figure()
    fig2.sp1 = fig2.add_subplot(111, projection="3d")
    fig2.sp1.plot(x, y, z)

    pyplot.show()

if __name__ == "__main__":
    main()
