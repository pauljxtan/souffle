"""
Discrete math.
"""

def factorial(n):
    """
    Computes the factorial of n.

    @type n: number

    @rtype: number
    @return: factorial of n
    """
    n = int(n)

    if n < 0:
        raise ValueError("This factorial function is undefined for negative "
                         "numbers")
    if n == 1:
        return 1
    return n * factorial(n - 1)

def binomial_coefficient(n, k):
    """
    Computes the coefficient of the x^k term in the binomial expansion of
    (1+x)^n. This quantity is also referred to as "n choose k" in
    combinatorics, that is, the number of ways to select k elements from a
    set of n elements. The family of binomial coefficients form Pascal's
    triangle, by way of Pascal's rule.

    @type n: number
    @type k: number

    @rtype: number
    @return: n choose k
    """
    return factorial(n) / (factorial(k) * factorial(n - k))
