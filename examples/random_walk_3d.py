#!/usr/bin/env python

"""
Simulating a 3-D random walk.
"""

from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from mathsci.math import stochastic

def main():
    # Initialize the walker
    pos0 = [50.0, 50.0, 50.0]
    lattice_dims = [100.0, 100.0, 100.0]
    walker = stochastic.RandomWalk3D(pos0, lattice_dims)

    # Take 10000 steps
    walker.walk(10000, True)
    x, y, z = walker.unpack()
    
    # Plot it
    fig1 = pyplot.figure()
    fig1_sp1 = fig1.add_subplot(111)
    fig1_sp1.plot(x, label="x")
    fig1_sp1.plot(y, label="y")
    fig1_sp1.plot(z, label="z")
    fig1_sp1.legend()

    # 3-D plot
    fig2 = pyplot.figure()
    fig2.sp1 = fig2.add_subplot(111, projection="3d")
    fig2.sp1.plot(x, y, z)

    pyplot.show()

if __name__ == "__main__":
    main()
