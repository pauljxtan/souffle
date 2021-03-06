"""
Miscellaneous utility functions.
"""

def frange(a, b, n):
    """
    Returns an equally spaced sequence of floats, in the interval [a, b], with
    n elements. (Essentially emulates the linspace() function in numpy.)

    @type  a: number
    @param a: start of interval
    @type  b: number
    @param b: end of interval
    @type  n: number
    @param n: length of sequence

    @rtype: iterable
    @return: sequence
    """
    if b <= a:
        raise ValueError("b should be larger than a")
    
    a = float(a)
    b = float(b)
    n = int(n)
    
    step = (b - a) / (n - 1)
    return [a + i * step for i in range(n)]

def same_sign(nums):
    """
    Returns True if all numbers in nums have the same sign; otherwise, returns
    False (including the case where at least one number is zero).

    @type  nums: iterable
    @param nums: list of numbers to check

    @rtype: boolean
    @return: whether the numbers all have the same sign
    """
    if not hasattr(nums, "__iter__"):
        raise ValueError("nums is not iterable")
    
    if (all([num < 0 for num in nums]) or all([num > 0 for num in nums])
        or all([num == 0 for num in nums])): 
        return True
    return False

def zeros(n):
    """
    Returns a sequence of zeros with n elements.
    
    @type  n: number
    @param n: length of sequence

    @rtype: list
    @return: sequence
    """
    return [0.0] * n

def ones(n):
    """
    Returns a sequence of ones with n elements.
    
    @type  n: number
    @param n: length of sequence

    @rtype: list
    @return: sequence
    """
    return [1.0] * n
