#!/usr/bin/env python

"""
Integrating the nonlinear pendulum.
"""

import math
from matplotlib import pyplot
from mathsci.physics import mechanics
from mathsci.math import odeint

def main():
    # Set the integration parameters
    f = mechanics.nonlinear_pendulum
    dt = 0.01
    t0 = 0.0
    X0 = [0.99*math.pi, 0.0]

    # Set constants
    l = 0.1

    # Integrate it...

    # Using non-adaptive RK4:
    #nonlinpend = odeint.RK4(f, t0, X0, l=l)
    #nonlinpend.integrate(dt, 2500, True)

    # Using adaptive RK4:
    nonlinpend = odeint.RK4Adaptive(f, t0, X0, l=l)
    duration = 25.0
    dt0 = 0.05
    delta = 1e-3
    indices = [0, 1]
    nonlinpend.integrate(duration, dt0, delta, indices, True)

    # Unpack data
    t = nonlinpend.t
    theta, omega = nonlinpend.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, theta, "x-")
    fig1_sp1.set_xlabel("Time [s]")
    fig1_sp1.set_ylabel("Angle from vertical [rad]")

    pyplot.show()

if __name__ == "__main__":
    main()
