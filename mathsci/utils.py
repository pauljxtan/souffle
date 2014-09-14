#!/usr/bin/env python

"""
Miscellaneous utility functions.
"""

def frange(a, b, n):
    """
    Returns an equally spaced sequence of floats, in the interval [a, b), with
    n elements.

    (Essentially emulates the linspace() function in numpy.)
    """
    if b <= a:
        raise ValueError("b should be larger than a")
    
    a = float(a)
    b = float(b)
    n = int(n)
    
    step = (b - a) / (n - 1)
    result = [a + i * step for i in range(n)]
    
    return result

def same_sign(nums):
    """
    Returns True if all numbers in nums have the same sign; otherwise, returns
    False (including the case where at least one number is zero).
    """
    if not hasattr(nums, "__iter__"):
        raise ValueError("nums is not iterable")
    
    if all(num < 0 for num in nums) or all(num > 0 for num in nums): 
        return True
    return False

def zeros(n):
    """
    Returns a sequence of zeros with n elements.
    """
    result = [0.0 for i in range(n)]
    
    return result

def ones(n):
    """
    Returns a sequence of ones with n elements.
    """
    result = [1.0 for i in range(n)]
    
    return result
