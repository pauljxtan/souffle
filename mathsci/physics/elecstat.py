"""
Electrostatics.
"""

import math
import mathsci.constants as const

def potential(q, r):
    """
    Returns the electric potential at distance r from a point charge q.

    @type  q: number
    @param q: source charge [C]
    @type  r: number
    @param r: distance from source [m]

    @rtype: number
    @return: electric potential at r [V]
    """
    q = float(q)
    r = float(r)
    return q / 4 / math.pi / const.eps_0 / r

def field(q, r):
    """
    Returns the magnitude of the electric field at distance r from a point
    charge q.

    @type  q: number
    @param q: source charge [C]
    @type  r: number
    @param r: distance from source [m]

    @rtype: number
    @return: electric field at r [N/C]
    """
    q = float(q)
    r = float(r)
    return q / 4 / math.pi / const.eps_0 / r**2
