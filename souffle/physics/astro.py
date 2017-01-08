"""
Astrophysics, celestial mechanics.
"""

import math
import souffle.constants as const
import souffle.datatypes as dtt
import souffle.physics.thermo as thermo

def orbit_1body(t, X, **kwargs):
    """
    The Newtonian equations of motion for orbit of a significantly less massive
    object (e.g. planet, comet) orbiting the Sun. 

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
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
    vx_dot = - const.G * const.M_sol * x / r**3
    vy_dot = - const.G * const.M_sol * y / r**3

    X_dot = [x_dot, y_dot, vx_dot, vy_dot]
    return dtt.Vector(X_dot)

def stellar_structure(r, X, **kwargs):
    """
    Solves the stellar structure equations of hydrostatic equilibrium and
    mass conservation.

    @type  r: number
    @param r: distance from center [m]
    @type  X: vector
    @param X: X[0] = M = enclosed mass at radius r [kg];
              X[1] = rho = density at radius r [kg m^{-3}]

    @rtype: vector
    @return: derivative vector
    """
    M = X[0]
    rho = X[1]

    # Get kwargs
    if len(kwargs) != 2:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: mu, T")

    # Hydrostatic equilibrium
    dP_dr = - const.G * M / r**2 * rho
    
    # Pressure
    P, dP_drho = thermo.ideal_gas_pressure(rho, kwargs['mu'], kwargs['T'])
    drho_dP = 1.0 / dP_drho
    drho_dr = drho_dP * dP_dr
    
    # Mass conservation
    dM_dr = 4 * math.pi * r**2 * rho
    
    X_dot = [dM_dr, drho_dr]
    
    return dtt.Vector(X_dot)
