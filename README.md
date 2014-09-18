mathsci
========
Python modules for computational science and mathematics. For personal education and amusement, only standard library modules are used (except in __examples__ where matplotlib is used for visualization), and clarity is greatly emphasized over performance. Absolutely not meant for serious applications -- one would certainly prefer numpy/scipy/etc. to my inefficient routines.

The documentation markup language is Epytext -- see the gh-pages branch (hosted on http://pauljxtan.github.io/mathsci) for the latest API docs.

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
    * TBC
* __utils__: miscellaneous utility functions

### Examples ###
* __integrate_lorenz_attractor__: integrates the Lorenz attractor in a chaotic regime
