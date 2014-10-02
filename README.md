mathsci
========
Python modules for computational science and mathematics. For personal education and amusement, only standard library modules are used (except in __examples__ where matplotlib is used for visualization), and clarity is greatly emphasized over performance. Not optimized for efficiency.

Documented in Epytext -- see the gh-pages branch (hosted on http://pauljxtan.github.io/mathsci) for the latest API docs.

See __tests__ for unit tests.

### Modules ###
* __constants__: various physical constants
* __datatypes__: generic datatypes
* __math__: the mathematical framework
    * __chaos__: chaotic dynamics
    * __derivative__: evaluating derivatives
    * __discrete__: discrete math
    * __integral__: evaluating integrals
    * __linalg__: fundamental linear algebra operations
    * __lineq__: solving linear equations
    * __maxmin__: finding maxima and minima of functions
    * __nonlineq__: solving nonlinear equations
    * __odeint__: integrating ordinary differential equations
    * __stochastic__: stochastic processes
* __physics__: physical applications
    * __astro__: astrophysics / celestial mechanics
    * __elecstat__: electrostatics
    * __mechanics__: mechanics
    * __oscillators__: oscillators
    * __thermo__: thermodynamics
* __utils__: miscellaneous utility functions

### Examples ###
* __electric_potential_field__: visualizing the electric potential and electric field of a source charge configuration
* __integrate_comet_orbit__: integrates a comet orbit
* __integrate_driven_pendulum__: integrating a driven pendulum
* __integrate_lorenz_attractor__: integrates the Lorenz attractor in a chaotic regime
* __integrate_nonlinear_pendulum__: integrating a nonlinear pendulum
* __integrate_predator_prey__: integrating the Lotka-Volterra equations to describe predator-prey dynamics
* __integrate_stellar_structure__: integrating the stellar structure equations of hydrostatic equilibrium and mass conservation to solve for the mass and density at a given temperature
* __integrate_vanderpol_oscillator__: integrating the van der Pol oscillator to find limit cycles
* __light_bulb__: investigating the efficiency of a light bulb
* __random_walk_3d__: simulating a 3-D random walk
* __telescope_diffraction_limit__: investigating the diffraction limit of a telescope
* __trig_funcs__: computing various trigonometric functions by solving nonlinear equations
* __wiens_displacement_constant__: solving a nonlinear equation to compute Wien's displacement constant, and use it to estimate the surface temperature of the Sun
