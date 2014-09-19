#!/usr/bin/env python

"""
Investigating the diffraction limit of a telescope.
"""

import math
from matplotlib import cm, pyplot
from mathsci.math import integral

def bessel_m(m, x):
    """
    Evaluates the m-th Bessel function at x.
    """
    integrand = lambda theta: math.cos(m * theta - x * math.sin(theta))
    J_m = 1.0 / math.pi * integral.simpsons(integrand, 0.0, math.pi, 1000)
    return J_m

def intensity(r, lam):
    """
    Computes the intensity of diffracted light.

    Parameters :
        r   : distance from center of diffraction pattern in focal plane
        lam : wavelength of light
    """
    r = float(r)
    lam = float(lam)

    k = 2 * math.pi / lam
    J_1 = bessel_m(1, k * r)
    I = (J_1 / k * r)**2
    return I

def main():

    # Wavelength of light
    lam = 500e-9

    # Set up the data grid
    plane_width = 1e-6
    plane_height = 1e-6
    n_rows = 50
    n_cols = 50
    grid = [[0.0 for i in range(n_rows)] for j in range(n_cols)]
    X = [(float(i) / n_rows - 0.5) * plane_width for i in range(n_rows)]
    Y = [(float(j) / n_cols - 0.5) * plane_height for j in range(n_cols)]

    # Compute intensities
    for i in range(n_rows):
        for j in range(n_cols):
            x = X[i]
            y = Y[j]
            r = math.sqrt(x**2 + y**2)
            grid[i][j] = intensity(r, lam)
        print i

    # Plot it
    #pyplot.imshow(grid.data, cmap=cm.Greys)
    pyplot.contourf(X, Y, grid)
    pyplot.colorbar()
    pyplot.show()

if __name__ == "__main__":
    main()
