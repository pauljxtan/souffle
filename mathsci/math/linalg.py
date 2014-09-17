"""
Provides fundamental linear algebra operations (Euclidean).
"""

import math
import mathsci.datatypes

def dot_product(A, B):
    """
    Computes the dot product of vectors A and B.

    @type A: vector
    @type B: vector

    @rtype: number
    @return: dot product of A and B
    """
    if len(A) != len(B):
        raise ValueError("Length of operands do not match")

    result = 0.0

    for i, v in enumerate(A):
        result += A[i] * B[i]

    return result

def cross_product(A, B):
    """
    Computes the cross product of vectors A and B.

    @type A: vector
    @type B: vector

    @rtype: vector
    @return: cross product of A and B
    """
    return

def determinant_minors(A):
    """
    Recursively computes the determinant of a square matrix A using expansion
    by minors.

    @type A: square matrix

    @rtype: number
    @return: determinant of A
    """
    if not isinstance(A, mathsci.datatypes.Matrix):
        raise ValueError("Operand is not mathsci.datatypes.Matrix")

    if A.n_rows != A.n_cols:
        raise ValueError("Operation is not square mathsci.datatypes.Matrix")

    n = A.n_rows

    # Check for trivial 1x1 case
    if n == 1:
        result = A.data[0][0]
        return result

    # Check for 2x2 case
    if n == 2:
        result = A.data[0][0] * A.data[1][1] - A.data[1][0] * A.data[0][1]
        return result

    result = 0.0
    for j1 in range(n):
        m = [[0.0 for i in range(n - 1)] for j in range(n - 1)]
        M = mathsci.datatypes.Matrix(m)
        for i in range(n):
            j2 = 0
            for j in range(n):
                if j == j1:
                    continue
                M.data[i - 1][j2] = A.data[i][j]
                j2 += 1
        result += (math.pow(-1, 1 + j1 + 1) * A.data[0][j1]
                   * determinant_minors(M))
    return result

def inverse(A):
    """
    Returns the inverse of a square matrix A.

    @type A: square matrix

    @rtype: matrix
    @return: inverse of A
    """
    return

if __name__ == "__main__":
    A = [1, 2, 3]
    B = [4, 5, 6]
    print dot_product(A, B)

    C = mathsci.datatypes.Matrix(
        [[ 0.40740418,  0.26988318,  0.65101212,  0.59384916],
         [ 0.85502017,  0.83792766,  0.88128841,  0.69794583],
         [ 0.74854304,  0.91927404,  0.13369317,  0.77294559],
         [ 0.54023376,  0.64533939,  0.97845268,  0.17995442]])
    print determinant_minors(C)
