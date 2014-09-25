"""
Oscillators.
"""

import mathsci.datatypes

##### Default constants #####
# Brusselator, unstable regime
BRUSS_A = 1.0
BRUSS_B = 3.0
# Lotka-Volterra
LOTKA_ALPHA = 1.5
LOTKA_BETA = 1.0
LOTKA_GAMMA = 2.0
LOTKA_DELTA = 1.0
# van der Pol oscillator
VANDERPOL_MU = 5.0
VANDERPOL_OMEGA = 1.0
#############################

def brusselator(t, X, **kwargs):
    """
    The Brusselator.

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    x = X[0]
    y = X[1]

    if len(kwargs) == 0:
        x_dot = 1 - (BRUSS_B + 1) * x + BRUSS_A * x**2 * y
        y_dot = BRUSS_B * x - BRUSS_A * x**2 * y
    elif len(kwargs) != 2:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: a, b")
    else:
        x_dot = 1 - (kwargs["b"] + 1) * x + kwargs["a"] * x**2 * y
        y_dot = kwargs["b"] * x - kwargs["a"] * x**2 * y

    X_dot = [x_dot, y_dot]
    return mathsci.datatypes.Vector(X_dot)

def lotka_volterra(t, X, **kwargs):
    """
    The Lotka-Volterra ("predator-prey") equations.

    We define the following constants:
    
    alpha = growth rate of prey
    beta  = rate at which predators consume prey
    gamma = death rate of predators
    delta = rate at which predators increase by consuming prey

    The prey population, x, increases at a rate of dx/dt = Ax, but is consumed
    by predators at a rate of dx/dt = -Bxy.

    The predator population, y, decreases at a rate of dy/dt = -Cy, but
    increases at a rate of dy/dt = Dxy.

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    x = X[0]
    y = X[1]

    if len(kwargs) == 0:
        x_dot = x * (LOTKA_ALPHA - LOTKA_BETA * y)
        y_dot = - y * (LOTKA_GAMMA - LOTKA_DELTA * x)
    elif len(kwargs) != 4:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: alpha, beta, gamma, delta")
    else:
        x_dot = x * (kwargs["alpha"] - kwargs["beta"] * y)
        y_dot = - y * (kwargs["gamma"] - kwargs["delta"] * x)

    X_dot = [x_dot, y_dot]
    return mathsci.datatypes.Vector(X_dot)

def vanderpol(t, X, **kwargs):
    """
    The van der Pol oscillator. This is a non-conservative oscillator, with
    nonlinear damping, that shows up in laser physics and electronic circuits.

    The system is described by
    
    d^2x/dx^2 - mu * (1 - x^2) * dx/dt + omega * x = 0
    
    where mu and omega are some constants.

    Applying the transformation y = dx/dt, we have the equations of motion
    
    y     = dx/dt
    dv/dt = mu * (1 - x^2) * v - omega^2 * x

    @type  t: number
    @param t: current time
    @type  X: vector
    @param X: current state

    @rtype: vector
    @return: derivative
    """
    x = X[0]
    y = X[1]

    if len(kwargs) == 0:
        x_dot = y
        y_dot = VANDERPOL_MU * (1 - x**2) * y - VANDERPOL_OMEGA**2 * x
    elif len(kwargs) != 2:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: mu, omega")
    else:
        x_dot = y
        y_dot = kwargs["mu"] * (1 - x**2) * y - kwargs["omega"]**2 * x

    X_dot = [x_dot, y_dot]
    return mathsci.datatypes.Vector(X_dot)
