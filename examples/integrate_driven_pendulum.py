#!/usr/bin/env python

"""
Integrating the driven pendulum.
"""

import math
from matplotlib import pyplot
from souffle.physics import mechanics
from souffle.math import odeint

def main():
    # Set the integration paramters
    f = mechanics.driven_pendulum
    dt = 0.0035
    t0 = 0.0
    X0 = [0.0, 0.0]

    # Set constants
    l = 0.1
    a = 5.0
    omegad = 10.0

    # Integrate it...

    # Using RK4:
    drivpend = odeint.RK4(f, t0, X0, l=l, a=a, omegad=omegad)
    drivpend.integrate(dt, 10000, True)

    # Unpack data
    t = drivpend.t
    theta, omega = drivpend.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, theta)
    fig1_sp1.set_xlabel("Time [s]")
    fig1_sp1.set_ylabel("Angle from vertical [rad]")

    pyplot.show()

if __name__ == "__main__":
    main()
