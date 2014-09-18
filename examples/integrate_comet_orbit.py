#!/usr/bin/env python

"""
Integrating a comet orbit in 2-D using adaptive ODE integration methods.

By Kepler's second law, the highly elongated orbit of a comet produces large
variations on its orbital velocity. Most of its orbit is spent at leisurely
velocities in the outer reaches of the Solar System, but occasionally it comes
close to the Sun for a fly-by and speeds up dramatically around perihelion.
This makes comet orbits great demonstrations for adaptive integration methods.
"""

from matplotlib import pyplot
from mathsci import datatypes
from mathsci.math import odeint
from mathsci.physics import astro

def main():
    # Set the initial conditions; we will place it in the vicinity of Neptune
    # The parameters are: x-position, y-position, x-velocity, y-velocity
    X0 = [4.0e12, 0, 0, 474.0]

    # Integrate it...
    orbit = astro.orbit_1body

    #---- Using adaptive RK4:
#    comet_orbit = odeint.RK4Adaptive(orbit, X0=X0)
    # Set duration of simulation
#    duration = 3e9
    # Choose some initial time-step size
#    dt0 = 30000.0
    # Set a target accuracy (AU per yr)
#    delta = 5e-2
    # The indices of the parameters in the state vector for which we want to
    # estimate the local truncation error
#    indices = [0, 1]
    # Integrate it!
#    comet_orbit.integrate(duration, dt0, delta, indices, True)
    #----
    
    #---- Using adaptive Bulirsch-Stoer:
    comet_orbit = odeint.BulStoAdaptive(orbit)

    # Set duration of simulation [s]
    duration = 3e9
    # Set a target accuracy [m/s]
    delta = 1e-7
    # Integrate it!
    comet_orbit.integrate(duration, delta, X0=X0, verbose=True)

    # Get the results
    t = comet_orbit.t
    x, y, v_x, v_y = comet_orbit.unpack()

    # Plot time-series of position and velocity
    fig1 = pyplot.figure()
    fig1.suptitle("Time series")
    fig1_sp1 = fig1.add_subplot(221)
    fig1_sp1.set_xlabel("t")
    fig1_sp1.set_ylabel("x")
    fig1_sp1.plot(t, x, ".")
    fig1_sp2 = fig1.add_subplot(222)
    fig1_sp2.set_xlabel("t")
    fig1_sp2.set_ylabel("y")
    fig1_sp2.plot(t, y, ".")
    fig1_sp3 = fig1.add_subplot(223)
    fig1_sp3.set_xlabel("t")
    fig1_sp3.set_ylabel("v_x")
    fig1_sp3.plot(t, v_x, ".")
    fig1_sp4 = fig1.add_subplot(224)
    fig1_sp4.set_xlabel("t")
    fig1_sp4.set_ylabel("v_y")
    fig1_sp4.plot(t, v_y, ".")

    # Plot the orbit
    fig2 = pyplot.figure()
    fig2_sp1 = fig2.add_subplot(111)
    fig2_sp1.set_title("Orbit")
    fig2_sp1.set_xlabel("x")
    fig2_sp1.set_ylabel("y")
    fig2_sp1.plot(x, y, ".")
    # Plot the sun
    fig2_sp1.plot(0.0, 0.0, "rx", label="Sun")

    # Plot the sequence of step sizes
    #fig3 = pyplot.figure()
    #fig3_sp1 = fig3.add_subplot(111)
    #fig3_sp1.set_title("Step sizes")
    #fig3_sp1.set_xlabel("t")
    #fig3_sp1.set_xlabel("dt")
    #fig3_sp1.plot(t, dt_all)

    pyplot.show()

if __name__ == "__main__":
    main()
