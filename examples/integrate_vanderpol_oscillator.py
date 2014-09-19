#!/usr/bin/env python

"""
Integrating the van der Pol oscillator.
"""

from matplotlib import pyplot
from mathsci.physics import oscillators
from mathsci.math import odeint

def main():
    # Set the integration paramters
    f = oscillators.vanderpol
    dt = 0.01
    t0 = 0.0
    X0 = [1.0, 0.0]

    # Set constants
    mu = 5.0
    omega = 1.0

    # Integrate it...

    # Using RK4:
    #vanderpol = odeint.RK4(f, t0, X0, mu=mu, omega=omega)
    #vanderpol.integrate(dt, 10000, True)

    # Using adaptive RK4:
    vanderpol = odeint.RK4Adaptive(f, t0, X0, mu=mu, omega=omega)
    duration = 100.0
    dt0 = 0.01
    delta = 1e-3
    indices = [0, 1]
    vanderpol.integrate(duration, dt0, delta, indices, True)

    # Unpack data
    t = vanderpol.t
    x, y = vanderpol.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, x, "x-", label="x")
    fig1_sp1.plot(t, y, "x-", label="y")
    fig1_sp1.legend()

    fig2 = pyplot.figure()
    fig2_sp1 = fig2.add_subplot(111)
    fig2_sp1.plot(x, y, "x-")
    fig2_sp1.set_title("Limit cycle")
    fig2_sp1.set_xlabel("x")
    fig2_sp1.set_ylabel("y")

    pyplot.show()

if __name__ == "__main__":
    main()
