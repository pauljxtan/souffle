#!/usr/bin/env python

"""
Integration of systems of ordinary differential equations, with non-adaptive
and adaptive methods.

See odeint_derivations.pdf for more detailed description.
"""

# TODO:
#   Spruce up the docstrings

import mathsci.datatypes

class OdeInt(object):
    """
    The base ODE integrator class.
    """
    def __init__(self, f, t0, X0, n_dims, kwargs):
        self.f = f
        self.t = []
        # X will be a list of Vectors
        self.X = []
        # These arguments are parameters apart from t and X that we want to
        # pass to the ODE function
        self.kwargs = kwargs

        # Set the initial conditions
        self.t.append(t0)
        if isinstance(X0, list) or isinstance(X0, tuple):
            if len(X0) == 0:
                if n_dims == None:
                    raise ValueError("ERROR: if no initial conditions given, "\
                                     "must specify number of dimensions")
                else:
                    X0 = [0.0] * int(n_dims)
                    X0 = mathsci.datatypes.Vector(X0)
            else:
                X0 = map(float, X0)
                X0 = mathsci.datatypes.Vector(X0)
        elif isinstance(X0, mathsci.datatypes.Vector):
            pass
        else:
            raise ValueError("Initial state is not list, tuple or Vector")
        self.X.append(X0)

    def integrate(self, dt, n_steps, verbose=False):
        """
        Integrates over multiple steps.

        Parameters  :
            dt      : length of time-step
            n_steps : number of steps to integrate
            verbose : print the state at each step [default=False]
        """
        dt = float(dt)
        n_steps = int(n_steps)

        for i in range(n_steps):
            t_new, X_new = self.step(dt)
            self.t.append(t_new)
            self.X.append(X_new)
            if verbose:
                self.current_state()

    def unpack(self):
        """
        Unpacks the data arrays.
        """
        all_data = [vector.data for vector in self.X]
        arrays = zip(*all_data)

        return arrays

    def current_state(self):
        """
        Outputs the current state.
        """
        print "%s\t%s" % (self.t[-1], " ".join(map(str, self.X[-1].data)))

class Euler(OdeInt):
    """
    Integrates a system of ODEs using the Euler method.
    
    Parameters :
        f      : vector function f(t, X) solving a system of ODEs
        t0     : initial time
        X0     : initial system state (default=[0.0, 0.0, ...])
        n_dims : number of dimensions (required if X0 is not given)
    """
    def __init__(self, f, t0=0.0, X0=[], n_dims=None, **kwargs):
        OdeInt.__init__(self, f, t0, X0, n_dims, kwargs)

    def step(self, dt):
        """
        Integrates a single step.
        """
        # Load the previous system state
        t = self.t[-1]
        X = self.X[-1]

        t_new = t + dt
        X_new = X + self.f(t, X, **self.kwargs).mul_scalar(dt)
        self.t.append(t_new)
        self.X.append(X_new)

        return t_new, X_new

class RK4(OdeInt):
    """
    Integrates a system of ODEs using the 4th order Runge-Kutta method.
    
    Parameters :
        f      : vector function f(t, X) solving a system of ODEs
        t0     : initial time
        X0     : initial system state (default=[0.0, 0.0, ...])
        n_dims : number of dimensions (required if X0 is not given)
    """
    ##########################################################
    #    The initial value problem is specified by         
    #        x_dot = f(t, x); x(t_0) = x_0
    #
    #    For a step size dt > 0, we define
    #        t[i+1] = t[i] + dt
    #        x[i+1] = x[i] + (1/6)(k_1 + 2k_2 + 2k_3 + k_4)
    #    for i = 0, 1, 2, ..., where
    #        k_1 = dt * f(t[i], x[i])
    #        k_2 = dt * f(t[i] + dt/2, x[i] + (dt/2)*k_1)
    #        k_3 = dt * f(t[i] + dt/2, x[i] + (dt/2)*k_2)
    #        k_4 = dt * f(t[i] + dt, x[i] + dt*k_3.
    #
    #    The vector X fully specifies the state of the system.
    ##########################################################
    def __init__(self, f, t0=0.0, X0=[], n_dims=None, **kwargs):
        OdeInt.__init__(self, f, t0, X0, n_dims, kwargs)

    def step(self, dt):
        """
        Integrates a single step.
        """
        # Load the previous system state
        t = self.t[-1]
        X = self.X[-1]

        # First increment
        K1 = self.f(t, X, **self.kwargs).mul_scalar(dt)
        # Second increment
        K2 = self.f(t + dt / 2, X + K1.div_scalar(2),
                    **self.kwargs).mul_scalar(dt)
        # Third increment
        K3 = self.f(t + dt / 2, X + K2.div_scalar(2),
                    **self.kwargs).mul_scalar(dt)
        # Fourth increment
        K4 = self.f(t + dt, X + K3, **self.kwargs).mul_scalar(dt)
        # Weighted average of increments
        K = (K1 + K2.mul_scalar(2) + K3.mul_scalar(2) + K4).div_scalar(6)

        t_new = t + dt
        X_new = X + K
        self.t.append(t_new)
        self.X.append(X_new)

        return t_new, X_new

class RK4Adaptive(OdeInt):
    """
    Integrates a system of ODEs using the 4th-order Runge-Kutta method, with
    adaptive step sizes.
    """
    def __init__(self, f, t0=0.0, X0=[], n_dims=None, **kwargs):
        OdeInt.__init__(self, f, t0, X0, n_dims, kwargs)
        self.dt_all = []

    def step(self, dt, t_override=None, X_override=None):
        """
        Integrates a single step.

        Parameters :
            dt         : size of the time-step
            t_override : if specified, overrides the latest element in the
                         time vector
            X_override : if specified, overrides the latest element in the
                         state vector
        """
        # Load the previous system state
        if t_override == None and X_override == None:
            t = self.t[-1]
            X = self.X[-1]
        else:
            t = t_override
            X = X_override

        # First increment
        K1 = self.f(t, X, **self.kwargs).mul_scalar(dt)
        # Second increment
        K2 = self.f(t + dt / 2, X + K1.div_scalar(2),
                    **self.kwargs).mul_scalar(dt)
        # Third increment
        K3 = self.f(t + dt / 2, X + K2.div_scalar(2), 
                    **self.kwargs).mul_scalar(dt)
        # Fourth increment
        K4 = self.f(t + dt, X + K3, **self.kwargs).mul_scalar(dt)
        # Weighted average of increments
        K = (K1 + K2.mul_scalar(2) + K3.mul_scalar(2) + K4).div_scalar(6)

        t_new = t + dt
        X_new = X + K

        return t_new, X_new

    def integrate(self, duration, dt0, delta, indices, verbose=False):
        """
        Integrates over a specified duration of time.

        Parameters :
            duration : total simulation time
            dt0      : initial size of time-step
            delta    : desired accuracy in state vector (per unit time)
            indices  : the indices of the parameters in the state vector for
                       which we want to estimate the local truncation error
        """
        dt = float(dt0)
        self.dt_all.append(dt)

        duration = float(duration)
        delta = float(delta)

        start_time = self.t[-1]
        while self.t[-1] < (start_time + duration):
            # Get the first estimate of X(t + 2*dt)
            t_new_1a, X_new_1a = self.step(dt)
            t_new_1b, X_new_1b = self.step(dt, t_new_1a, X_new_1a)
            # Get the second estimate of X(t + 2*dt)
            t_new_2, X_new_2 = self.step(2 * dt)
            # Compute the error
            error = self.step_error(X_new_1b, X_new_2, indices)
            rho = delta * dt / error

            # If rho > 1: don't need to redo step; update step size and
            #             immediately go to next iteration
            if rho > 1:
                t_new, X_new = t_new_1a, X_new_1a
                self.t.append(t_new)
                self.X.append(X_new)
                self.dt_all.append(dt)
                # Adjust step size for next iteration
                dt *= rho**0.25
            # If rho < 1: update step size, redo step, and then move on to
            #             next iteration
            elif rho < 1:
                # Adjust step size for redo
                dt *= rho**0.25
                t_new, X_new = self.step(dt)
                self.t.append(t_new)
                self.X.append(X_new)
                self.dt_all.append(dt)

            if verbose:
                self.current_state()

    def step_error(self, X1, X2, indices):
        """
        Estimates the local trunctation error from the two estimates of
        X(t + 2*dt).

        For RK4, this per-step error is given by
            epsilon = c*dt^5 = (1/30)(x1 - x2)

        Parameters :
            X1      : estimate of X(t + 2*dt) with two iterations with size dt
            X2      : estimate of X(t + 2*dt) with one iteration of size 2*dt
            indices : the indices of the parameters in the state vector for
                      which we want to estimate the local truncation error
        """
        epsilons = [1.0 / 30 * (X1.data[i] - X2.data[i]) for i in indices]
        epsilons_sumsq = sum([epsilon**2 for epsilon in epsilons])
        #error = pow(epsilons_sumsq, 1.0 / len(indices))
        error = pow(epsilons_sumsq, 0.5)

        return error

class BulSto(OdeInt):
    """
    Integrates a system of ODEs using the Bulirsch-Stoer method.
    
    Parameters :
        f      : vector function f(t, X) solving a system of ODEs
        t0     : initial time
        X0     : initial system state (default=[0.0, 0.0, ...])
        n_dims : number of dimensions (required if X0 is not given)
    """
    def __init__(self, f, t0=0.0, X0=[], n_dims=None, **kwargs):
        OdeInt.__init__(self, f, t0, X0, n_dims, kwargs)

    def step(self, dt, delta):
        """
        Integrates a single step.
        """
        # Load the previous system state
        t = self.t[-1]
        X = self.X[-1]

        # Take a first midpoint step of size dt
        n = 1
        X1 = X + self.f(t, X, **self.kwargs).mul_scalar(dt / 2)
        X2 = X + self.f(t, X1, **self.kwargs).mul_scalar(dt)

        # Compute the first row of the extrapolation table
        e1 = [(X1 + X2 + self.f(t, X2, **self.kwargs)
               .mul_scalar(dt / 2)).div_scalar(2), ]

        # Extrapolate for an increasing number of rows until the desired
        # accuracy is achieved
        error = 2 * dt * delta
        while error > dt * delta:
            n += 1
            ddt = dt / n

            # Take midpoint step of size ddt
            X1 = X + self.f(t, X, **self.kwargs).mul_scalar(ddt / 2)
            X2 = X + self.f(t, X1, **self.kwargs).mul_scalar(ddt)
            for i in range(n - 1):
                X1 += self.f(t, X2, **self.kwargs).mul_scalar(ddt)
                X2 += self.f(t, X1, **self.kwargs).mul_scalar(ddt)

            # e2 records the previous e1; used for error estimation later
            e2 = e1
            e1 = [mathsci.datatypes.Vector([0.0 for i in enumerate(X)])
                  for j in range(n)]
            e1[0] = (X1 + X2 + self.f(t, X2, **self.kwargs)
                     .mul_scalar(ddt / 2)).div_scalar(2)

            # Extrapolate the remaining rows
            for m in range(1, n):
                epsilon = ((e1[m - 1] - e2[m - 1])
                         .div_scalar((float(n) / (n - 1))**(2*m) - 1))
                e1[m] = e1[m - 1] + epsilon
            error = abs(epsilon[0])

        # Take the most accurate estimate
        t_new = t + dt
        X_new = e1[n - 1]

        return t_new, X_new
    
    def integrate(self, dt, n_steps, delta, verbose=False):
        """
        Integrates over multiple steps.

        Parameters  :
            dt      : length of time-step
            n_steps : number of steps to integrate
            delta   : desired accuracy per unit time
            verbose : print the state at each step [default=False]
        """
        dt = float(dt)
        n_steps = int(n_steps)
        delta = float(delta)

        for i in range(n_steps):
            t_new, X_new = self.step(dt, delta)
            self.t.append(t_new)
            self.X.append(X_new)
            if verbose:
                self.current_state()

class BulStoAdaptive(OdeInt):
    """
    Integrates a system of ODEs using the Bulirsch-Stoer method, with adaptive
    step sizes. 

    This class is a little different from the others since the integration is
    performed recursively:
        (1) There is no step() method
        (2) The initial conditions are passed to the integrate() method instead
            of the constructor
    
    Parameters :
        f      : vector function f(t, X) solving a system of ODEs
    """
    def __init__(self, f, **kwargs):
        self.f = f
        self.t = []
        self.X = []
        self.kwargs = kwargs

    def integrate(self, duration, delta, t0=0.0, X0=[], n_dims=None, nmax=8,
                  verbose=False):
        """
        Resursively performs the steps of adaptive Bulirsch-Stoer.

        Parameters   :
            duration : total length of the simulation
            delta    : desired accuracy
            t0       : initial time [default=0.0]
            X0       : initial system state [default=[0.0, 0.0,..., 0.0]
            n_dims   : number of dimensions (required if X0 is not given)
            nmax     : maximum subdivisions of the current time-step
            verbose  : print the state at each step [default=False]
        """
        if isinstance(X0, list) or isinstance(X0, tuple):
            if len(X0) == 0:
                if n_dims == None:
                    raise ValueError("ERROR: if no initial conditions given, "\
                                     "must specify number of dimensions")
                else:
                    X0 = [0.0] * int(n_dims)
                    X0 = mathsci.datatypes.Vector(X0)
            else:
                X0 = map(float, X0)
                X0 = mathsci.datatypes.Vector(X0)
        elif isinstance(X0, mathsci.datatypes.Vector):
            pass
        else:
            raise ValueError("Initial state is not list, tuple or Vector")
        dt = duration
        t = t0
        X = X0

        # Take a first midpoint step of size dt
        n = 1
        X1 = X + self.f(t, X, **self.kwargs).mul_scalar(dt / 2)
        X2 = X + self.f(t, X1, **self.kwargs).mul_scalar(dt)

        # Compute the first row of the extrapolation table
        e1 = [(X1 + X2 + self.f(t, X2, **self.kwargs)
               .mul_scalar(dt / 2)).div_scalar(2), ]

        # Extrapolate for an increasing number of rows until the desired
        # accuracy is achieved, or the maximum number of steps is reached
        for i in range(2, nmax + 1):
            n += 1
            ddt = dt / n

            # Take midpoint step of size ddt
            X1 = X + self.f(t, X, **self.kwargs).mul_scalar(ddt / 2)
            X2 = X + self.f(t, X1, **self.kwargs).mul_scalar(ddt)
            for i in range(n - 1):
                X1 += self.f(t, X2, **self.kwargs).mul_scalar(ddt)
                X2 += self.f(t, X1, **self.kwargs).mul_scalar(ddt)

            # Compute n rows of extrapolation table (list of Vectors)
            e2 = e1
            e1 = [mathsci.datatypes.Vector([0.0 for i in enumerate(X)])
                  for j in range(n)]
            e1[0] = (X1 + X2 + self.f(t, X2, **self.kwargs)
                     .mul_scalar(ddt / 2)).div_scalar(2)
            for m in range(1, n):
                epsilon = ((e1[m - 1] - e2[m - 1])
                         .div_scalar((float(n) / (n - 1))**(2*m) - 1))
                e1[m] = e1[m - 1] + epsilon
            error = abs(epsilon[0])

            # If the desired accuracy has been achieved, return the values
            if error < dt * delta:
                # Take the most accurate estimate
                t_new = t + dt
                X_new = e1[n - 1]
                self.t.append(t_new)
                self.X.append(X_new)
                if verbose:
                    self.current_state()
                    #print "%s\t%s" % (t_new," ".join(map(str, X_new[-1].data)))

                return t_new, X_new

        # If desired accuracy was not achieved at n=nmax, apply the method
        # recursively to sub-intervals of size dt / 2
        t_new_1, X_new_1 = self.integrate(dt/2, delta, t, X)
        t_new_2, X_new_2 = self.integrate(dt/2, delta, t_new_1, X_new_1)
            
        return t_new_2, X_new_2
