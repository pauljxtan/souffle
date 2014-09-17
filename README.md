mathsci
========
Python modules for computational science and mathematics. For personal education and amusement, only standard library modules are used (except in __examples__ where matplotlib is used for visualization), and clarity is greatly emphasized over performance. Absolutely not meant for serious applications -- one would certainly prefer numpy/scipy/etc. to my inefficient routines.

The documentation markup language is Epytext -- see __apidocs__ for the latest API docs.

### Modules ###
* __constants__: various physical constants
* __datatypes__: generic datatypes
* __math__: the mathematical framework
    * __chaos__: chaotic dynamics
    * __linalg__: fundamental linear algebra operations
    * __odeint__: integrating ordinary differential equations
* __utils__: miscellaneous utility functions

### Examples ###
* __integrate_lorenz_attractor__: integrates the Lorenz attractor in a chaotic regime
