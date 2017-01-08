"""
Chaotic dynamics.
"""
import souffle.datatypes as dtt

##### Default constants #####
LORENZ_SIGMA = 10.0
LORENZ_BETA = 8.0 / 3.0
LORENZ_RHO = 28.0
#############################

def lorenz_attractor(t, X, **kwargs):
    """
    The Lorenz attractor.
    
    @type  t: number
    @param t: current time
    @type  X: vector 
    @param X: current state
    
    @rtype: vector
    @return: derivative
    """
    x = X[0]
    y = X[1]
    z = X[2]

    if len(kwargs) == 0:
        # Use defaults
        x_dot = LORENZ_SIGMA * (y - x)
        y_dot = x * (LORENZ_RHO - z) - y
        z_dot = x * y - LORENZ_BETA * z
    elif len(kwargs) != 3:
        raise ValueError("Bad kwargs; please provide all of the "\
                         "following parameters: sigma, rho, beta")
    else:
        x_dot = kwargs["sigma"] * (y - x)
        y_dot = x * (kwargs["rho"] - z) - y
        z_dot = x * y - kwargs["beta"] * z

    X_dot = [x_dot, y_dot, z_dot]
    return dtt.Vector(X_dot)
