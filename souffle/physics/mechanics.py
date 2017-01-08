"""
Mechanics.
"""

import math
import souffle.datatypes as dtt
import souffle.constants as const

##### Default constants #####
# Nonlinear pendulum
NONLINPEND_L = 0.1
# Driven pendulum
DRIVPEND_L = 0.1
DRIVPEND_A = 5.0
DRIVPEND_OMEGAD = 10.0
#############################

def nonlinear_pendulum(t, X, **kwargs):
    """
    The nonlinear pendulum.

    The pendulum has length L with attached mass m, with theta denoting the
    angle from vertical. We ignore friction and assume a massless pendulum.

    The acceleration of the mass is
    
    a = L * d^2theta/dtheta^2
    
    The force on the mass is
    
    F = m * g
    
    with tangential component m * g * sin(theta).

    Thus by Newton's 2nd law, the angular acceleration is
    
    m * L * d^2theta/dtheta^2 = - m * g * sin(theta)
    d^2theta/dtheta^2 = - (g / L) * sin(theta)

    To convert this to a first-order system, we define the angular velocity
    
    omega = dtheta/dt
    
    and rewrite the angular acceleration as
    
    domega/dt = - (g / L) * sin(theta)

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    theta = X[0]
    omega = X[1]

    if len(kwargs) == 0:
        theta_dot = omega
        omega_dot = (-(const.g / NONLINPEND_L)
                     * math.sin(theta))
    elif len(kwargs) != 1:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: l")
    else:
        theta_dot = omega
        omega_dot = (-(const.g / kwargs["l"])
                     * math.sin(theta))

    X_dot = [theta_dot, omega_dot]
    return dtt.Vector(X_dot)

def driven_pendulum(t, X, **kwargs):
    """
    The driven pendulum. Adds an oscillatory force exerted on the mass to the
    nonlinear pendulum.
    (See nonlinear_pendulum() for more derivation.)

    The equations of motion are:
 
    omega     = dtheta/dt
    domega/dt = - (g / L) * sin(theta) + A * cos(theta) * sin(omega_d * t)
 
    where omega_d is the angular driving force and A is some constant.

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    theta = X[0]
    omega = X[1]

    if len(kwargs) == 0:
        theta_dot = omega
        omega_dot = (-(const.g / DRIVPEND_L) * math.sin(theta)
                     + DRIVPEND_A * math.cos(theta)
                     * math.sin(DRIVPEND_OMEGAD*t))
    elif len(kwargs) != 3:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: l, a, omegad")
    else:
        theta_dot = omega
        omega_dot = (-(const.g / kwargs["l"]) * math.sin(theta)
                     + kwargs["a"] * math.cos(theta)
                     * math.sin(kwargs["omegad"]*t))

    X_dot = [theta_dot, omega_dot]
    return dtt.Vector(X_dot)

# TODO
def double_pendulum(t, X, **kwargs):
    """
    The double pendulum.

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    theta_1 = X[0]
    theta_2 = X[1]
    p_1 = X[2]
    p_2 = X[3]

    # ...

    return

# TODO
def symmetric_top(t, X, **kwargs):
    """
    The symmetric top.

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    theta = X[0]
    phi = X[1]
    psi = X[2]
    theta_dot = X[3]
    phi_dot = X[4]
    psi_dot = X[5]

    # ...

    return
