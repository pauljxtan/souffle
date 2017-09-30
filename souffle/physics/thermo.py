"""
Thermodynamics.
"""

import math
import souffle.constants as const
from souffle.datatypes import Vector

def ideal_gas_pressure(rho, mu, T):
    """
    Returns the ideal gas pressure and its derivative with respect to density.

    @type  rho: number
    @param rho: density [kg m^{-3}]
    @type   mu: number
    @param  mu: average particle mass [kg]
    @type    T: number
    @param   T: temperature [K]

    @rtype: number, number
    @return: pressure, first derivative of pressure
    """
    P = rho / (mu * const.m_H) * const.k_B * T
    # Derivative w.r.t density
    dP_drho = 1.0 / (mu * const.m_H) * const.k_B * T

    return P, dP_drho

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
    if len(kwargs) != 3:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: rho, mu, T")

    # Hydrostatic equilibrium
    dP_dr = - const.G * M / r**2 * kwargs['rho']
    
    # Pressure
    P, dP_drho = ideal_gas_pressure(kwargs['rho'], kwargs['mu'], kwargs['T'])
    drho_dP = 1.0 / dP_drho
    drho_dr = drho_dP * dP_dr
    
    # Mass conservation
    dM_dr = 4 * math.pi * r**2 * kwargs['rho']
    
    X_dot = [dM_dr, drho_dr]
    
    return Vector(X_dot)
