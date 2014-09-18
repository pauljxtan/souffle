"""
Astrophysics, celestial mechanics.
"""

import mathsci.constants
import mathsci.datatypes

def orbit_1body(t, X, **kwargs):
    """
    The Newtonian equations of motion for orbit of a significantly less massive
    object (e.g. planet, comet) orbiting the Sun. 

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: evolved state
    """
    x = X[0]
    y = X[1]
    vx = X[2]
    vy = X[3]

    # Orbital separation
    r = (x**2 + y**2)**0.5

    # Solve the ODEs
    x_dot = vx
    y_dot = vy
    vx_dot = - mathsci.constants.G * mathsci.constants.M_sol * x / r**3
    vy_dot = - mathsci.constants.G * mathsci.constants.M_sol * y / r**3

    X_dot = [x_dot, y_dot, vx_dot, vy_dot]
    return mathsci.datatypes.Vector(X_dot)
