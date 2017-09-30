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


    try:
        sigma = kwargs['sigma']
        rho = kwargs['rho']
        beta = kwargs['beta']
    except:
        print("Unable to read parameters from input, using defaults")
        sigma = LORENZ_SIGMA
        rho = LORENZ_RHO
        beta = LORENZ_BETA

    x_dot = sigma * (y - x)
    y_dot = x * (rho - z) - y
    z_dot = x * y - beta * z

    X_dot = [x_dot, y_dot, z_dot]
    return dtt.Vector(X_dot)
