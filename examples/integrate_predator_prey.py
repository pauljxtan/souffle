#!/usr/bin/env python

"""
Integrating the Lotka-Volterra ("predator-prey") equations.
"""

from matplotlib import pyplot
from souffle.physics import oscillators
from souffle.math import odeint

def main():
    # Set the integration paramters
    f = oscillators.lotka_volterra
    dt = 0.05
    t0 = 0.0
    X0 = [10.0, 5.0]

    # Set constants
    alpha = 1.5
    beta = 1.0
    gamma = 2.0
    delta = 1.0

    # Integrate it...

    # Using non-adaptive RK4:
    #lotka = odeint.RK4(f, t0, X0, alpha=alpha, beta=beta, gamma=gamma, delta=delta)
    #lotka.integrate(dt, 500, True)
    
    # Using adaptive RK4:
    lotka = odeint.RK4Adaptive(f, t0, X0, alpha=alpha, beta=beta, gamma=gamma, delta=delta)
    duration = 50.0
    dt0 = 0.05
    delta = 1e-4
    indices = [0, 1]
    lotka.integrate(duration, dt0, delta, indices, True)

    # Unpack data
    t = lotka.t
    x, y = lotka.unpack()

    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(t, x, "bx-", label="Rabbits")
    fig1_sp1.plot(t, y, "rx-", label="Foxes")
    fig1_sp1.set_xlabel("Time")
    fig1_sp1.set_ylabel("Population")
    fig1_sp1.legend()

    pyplot.show()

if __name__ == "__main__":
    main()
