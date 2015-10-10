"""
Miscellaneous mathematical objects.
"""

def continued_fraction(N, D, k):
    """
    Computes a generalized finite continued fraction with k terms.

    @type  N: function N(int)
    @param N: a function that returns the numerator in the i-th term
    @type  D: function D(int)
    @param D: a function that returns the denominator in the i-th term
    @type  k: int
    @param k: number of terms

    (Motivated by a neat exercise in SICP. Feel free to check out
    https://github.com/pauljxtan/miscellany/tree/master/sicp_exs
    for Scheme solutions to this exercise as well as many others.)
    """
    return continued_fraction_recursive(N, D, k, 1)

def continued_fraction_recursive(N, D, k, i):
    """
    Recursively computes the i-th term of a generalized finite continued
    fraction. Use the wrapper function continued_fraction(N, D, k) instead
    of this one.

    @type  N: function(int)
    @param N: a function that returns the numerator in the i-th term
    @type  D: function(int)
    @param D: a function that returns the denominator in the i-th term
    @type  k: int
    @param k: total number of terms
    @type  i: int
    @param i: index of this term
    """
    if i == k:
        return 1
    return N(i) / (D(i) + continued_fraction_recursive(N, D, k, i + 1))
