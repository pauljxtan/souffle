#!/usr/bin/env python

"""
An example for computing the electric potential and electric field on a plane.
"""

import math
from matplotlib import pyplot
from souffle.physics import elecstat

def main():
    # Set the grid dimensions
    n_rows = 100
    n_cols = 100
    spacing = 0.001
    print("Using a %d-by-%d grid with %fm spacing" % (n_rows, n_cols, spacing))

    # Initialize the grid for the potential
    V = [[0.0 for i in range(n_rows)] for j in range(n_cols)]
    # Initialize the grid for the x- and y-components of the electric field
    E_x = [[0.0 for i in range(n_rows)] for j in range(n_cols)]
    E_y = [[0.0 for i in range(n_rows)] for j in range(n_cols)]

    # Place the source charge(s) on the grid
    # The following tuples have the form: (charge, x-coordinate, y-coordinate)
    q_1 = (+1.0, 0.5 * n_rows * spacing, 0.25 * n_cols * spacing)
    q_2 = (-1.0, 0.5 * n_rows * spacing, 0.75 * n_cols * spacing)
    sources = [q_1, q_2]

    # Compute the potential at all points on the grid
    print("Computing potential...")
    for i in range(n_rows):
        for j in range(n_cols):
            x = i * spacing
            y = j * spacing

            # Flag indicating whether (x, y) is at a source charge
            at_source = False

            # Check if (x, y) is at any of the source charges
            for source in sources:
                if (x, y) == (source[1], source[2]):
                    at_source = True
                    break

            if at_source:
                continue
            else:
                for source in sources:
                    # Get the distance between (x, y) and this source charage
                    r = math.sqrt((x - source[1])**2 + (y - source[2])**2)
                    # Add the potential contribution from this source charge
                    V[i][j] += elecstat.potential(source[0], r)
    
    # Make a contour plot
    pyplot.contour(range(n_rows), range(n_cols), V, n_rows)
    pyplot.show()

if __name__ == "__main__":
    main()

