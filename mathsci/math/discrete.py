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

    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1

def binomial_coefficient(n, k):
    """
    Computes "n choose k".

    @type n: number
    @type k: number

    @rtype: number
    @return: n choose k
    """
    return factorial(n) / (factorial(k) * factorial(n - k))

if __name__ == "__main__":
    print "10! =", factorial(10)
    print "4 choose 2 =", binomial_coefficient(4, 2)
