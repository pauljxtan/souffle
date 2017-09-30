"""
Stochastic processes.
"""

# TODO:
#     Generalize lattice_dims to have non-zero minimum
#     Example script with real-time plotting

import random

class RandomWalk(object):
    """
    The base random walk class.
    """
    def __init__(self, dims, pos0, lattice_dims, kwargs):
        self.pos = []

        if dims == 1:
            if isinstance(pos0, int) or isinstance(pos0, float):
                self.pos.append(int(pos0))
            elif pos0 is None:
                self.pos.append(0)
            else:
                raise ValueError("Initial position is not int or float")

            if (isinstance(lattice_dims, int)
                or isinstance(lattice_dims, float)):
                self.lattice_dims = lattice_dims
            elif lattice_dims is None:
                self.lattice_dims = None
            else:
                raise ValueError("Input lattice dim is not int or float")

        else:
            if isinstance(pos0, list) or isinstance(pos0, tuple):
                if len(pos0) == dims:
                    self.pos.append(tuple(map(int, pos0)))
                else:
                    raise ValueError("Initial position has wrong dimensions")
            elif pos0 is None:
                self.pos.append([0, 0])
            else:
                raise ValueError("Initial position is not list or tuple")

            if (isinstance(lattice_dims, list)
                or isinstance(lattice_dims, tuple)):
                if len(lattice_dims) == dims:
                    self.lattice_dims = tuple(lattice_dims)
                else:
                    raise ValueError("Input lattice has wrong dimensions")
            elif lattice_dims is None:
                self.lattice_dims = lattice_dims
            else:
                raise ValueError("Input lattice dims is not list or tuple")

        self.kwargs = kwargs

    def get_position(self):
        return self.pos[-1]
    
    def get_trajectory(self):
        return self.pos

    def unpack(self):
        arrays = zip(*self.pos)
        return arrays

    def current_position(self):
        print(" ".join(map(str, self.pos[-1])))

class RandomWalk1D(RandomWalk):
    """
    Performs a random walk in one dimension.
    """
    def __init__(self, pos0=None, lattice_dims=None, **kwargs):
        RandomWalk.__init__(self, 1, pos0, lattice_dims, kwargs)
    
    def step(self):
        """
        Takes a single step.

        @rtype: number
        @return: new position
        """
        direction = random.randint(1, 2)
        if direction == 1:
            # Move right
            new_pos = self.pos[-1] + 1
        else:
            # Move left
            new_pos = self.pos[-1] - 1

        return new_pos

    def walk(self, n_steps, verbose=False):
        """
        Takes multiple steps.

        @type  n_steps: number
        @param n_steps: number of steps
        @type  verbose: boolean
        @param verbose: print position at each step [default=False]
        """
        for n in range(n_steps):
            new_pos = self.step()
            
            # Keep the particle within the lattice dimensions
            while (new_pos < 0 or new_pos > self.lattice_dims):
                new_pos = self.step()
            
            self.pos.append(new_pos)

            if verbose:
                self.current_position()

class RandomWalk2D(RandomWalk):
    """
    Performs a random walk in two dimensions.
    """
    def __init__(self, pos0=None, lattice_dims=None, **kwargs):
        RandomWalk.__init__(self, 2, pos0, lattice_dims, kwargs)

    def step(self):
        """
        Takes a single step.

        @rtype: vector
        @return: new position
        """
        direction = random.randint(1, 4)
        if direction == 1:
            # Move right
            new_pos = (self.pos[-1][0] + 1, self.pos[-1][1])
        elif direction == 2:
            # Move left
            new_pos = (self.pos[-1][0] - 1, self.pos[-1][1])
        elif direction == 3:
            # Move up
            new_pos = (self.pos[-1][0] + 1, self.pos[-1][1])
        else:
            # Move down
            new_pos = (self.pos[-1][0] + 1, self.pos[-1][1])

        return new_pos

    def walk(self, n_steps, verbose=False):
        """
        Takes multiple steps.

        @type  n_steps: number
        @param n_steps: number of steps
        @type  verbose: boolean
        @param verbose: print position at each step [default=False]
        """
        for n in range(n_steps):
            new_pos = self.step()
            
            # Keep the particle within the lattice dimensions
            while (new_pos[0] < 0 or new_pos[0] > self.lattice_dims[0]
                   or new_pos[1] < 0 or new_pos[1] > self.lattice_dims[1]):
                new_pos = self.step()
            self.pos.append(new_pos)

            if verbose:
                self.current_position()

class RandomWalk3D(RandomWalk):
    """
    Performs a random walk in three dimensions.
    """
    def __init__(self, pos0=None, lattice_dims=None, **kwargs):
        RandomWalk.__init__(self, 3, pos0, lattice_dims, kwargs)

    def step(self):
        """
        Takes a single step.

        @rtype: vector
        @return: new position
        """
        direction = random.randint(1, 6)
        if direction == 1:
            # Move up on x-axis
            new_pos = (self.pos[-1][0] + 1, self.pos[-1][1], self.pos[-1][2])
        elif direction == 2:
            # Move down on x-axis
            new_pos = (self.pos[-1][0] - 1, self.pos[-1][1], self.pos[-1][2])
        elif direction == 3:
            # Move up on y-axis
            new_pos = (self.pos[-1][0], self.pos[-1][1] + 1, self.pos[-1][2])
        elif direction == 4:
            # Move down on y-axis
            new_pos = (self.pos[-1][0], self.pos[-1][1] - 1, self.pos[-1][2])
        elif direction == 5:
            # Move up on z-axis
            new_pos = (self.pos[-1][0], self.pos[-1][1], self.pos[-1][2] + 1)
        else:
            # Move down on z-axis
            new_pos = (self.pos[-1][0], self.pos[-1][1], self.pos[-1][2] - 1)

        return new_pos

    def walk(self, n_steps, verbose=False):
        """
        Takes multiple steps.

        @type  n_steps: number
        @param n_steps: number of steps
        @type  verbose: boolean
        @param verbose: print position at each step [default=False]
        """
        for n in range(n_steps):
            new_pos = self.step()
            
            # Keep the particle within the lattice dimensions
            while (new_pos[0] < 0 or new_pos[0] > self.lattice_dims[0]
                   or new_pos[1] < 0 or new_pos[1] > self.lattice_dims[1]
                   or new_pos[2] < 0 or new_pos[2] > self.lattice_dims[2]):
                new_pos = self.step()
            
            self.pos.append(new_pos)

            if verbose:
                self.current_position()

if __name__ == "__main__":
    walk1d = RandomWalk1D(1, 10)
    walk1d.walk(100)
    print(walk1d.get_position())
    print(walk1d.get_trajectory())
    print()
    walk2d = RandomWalk2D([2, 3], [10, 10])
    walk2d.walk(100)
    print(walk2d.get_position())
    print(walk2d.get_trajectory())
    print()
    walk3d = RandomWalk3D([4, 5, 6], [10, 10, 10])
    walk3d.walk(100)
    print(walk3d.get_position())
    print(walk3d.get_trajectory())
