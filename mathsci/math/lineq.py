"""
Solving systems of linear equations.
"""

# TODO:
#     Modify gauss_elim() to use Matrix class

import mathsci.datatypes as dt

def gauss_elim(A, b):
    """
    Performs Gaussian elimination, with partial pivoting and backsubstition,
    to solve the simultaneous linear equations given by Ax = b.

    @type  A: matrix
    @param A: coefficient matrix of shape m x n
    @type  b: vector
    @param b: RHS vector of length m
        
    @rtype: vector
    @return: solution vector of length m
    """
    if not (isinstance(A, dt.Matrix)
            or isinstance(A, list) or isinstance(A, tuple)):
        raise ValueError("A is not Matrix, list or tuple")
    if not (isinstance(b, list) or isinstance(b, tuple)):
        raise ValueError("b is not list or tuple")

    if isinstance(A, dt.Matrix):
        A = A.data
    b = map(float, b)

    n_rows = len(A)
    n_cols = len(A[0])

    x = [0.0 for row in range(n_rows)]

    for i in range(n_rows):
        #---- Do partial pivoting
        # Check if this row needs to be swapped
        # Get the i-th column
        tmp = [A[j][i] for j in range(n_rows)]
        # Get distance of each element from zero along the i-th column
        diffs = [abs(elem) for elem in tmp]
        # Get the row index of the pivot element (farthest from zero)
        pivot_idx = diffs.index(max(diffs))
        # If the pivot element is not in the i-th row and not in a higher row
        if pivot_idx > i:
            # Swap the i-th row with the pivot row
            tmp = A[i], b[i]
            A[i], b[i] = A[pivot_idx], b[pivot_idx]
            A[pivot_idx], b[pivot_idx] = tmp
        #----
        # Divide the i-th element of the i-th row from the i-th row, both sides
        tmp = A[i][i]
        for k in range(n_cols):
            A[i][k] /= tmp
        b[i] /= tmp
        for m in range(i + 1, n_rows):
            # Subtract (the i-th element of the m-th row) * (the i-th row)
            #     from each m-th row, on both sides
            tmp = A[m][i]
            for n in range(n_cols):
                A[m][n] -= tmp * A[i][n]
            b[m] -= tmp * b[i]
    #---- Do backsubstitution
    # Start with the lowest row
    for i in range(n_rows - 1, -1, -1):
        # The first term is the i-th element of b
        x[i] = b[i]
        # The remaining term(s) come from lower rows
        for j in range(i + 1, n_rows):
            x[i] -= A[i][j] * x[j]

    return x
