"""
Provides generic datatypes.
"""

# TODO:
#     define __getitem__ for Vector and Matrix
#     define slicing methods for Vector and Matrix
#     define all useful magic methods (most of them)
#     add more type checking

import mathsci.math.linalg

ERR_INPUT_NOT_LIST_TUPLE = "Input data is not list or tuple"
ERR_INPUT_BAD_DIMS = "Input data has incompatible dimensions"
ERR_KEY_NOT_INT_LIST_TUPLE = "key is not int, list or tuple"
ERR_OP_BAD_DIMS = "Operand has incompatible dimensions for element-wise operation"
ERR_OP_NOT_VEC = "Operand is not Vector"
ERR_OP_NOT_MAT = "Operand is not Matrix"

class Vector(object):
    """
    The generic vector class.
    """
    def __init__(self, data=None):
        if data == None:
            self.data = []
        else:
            if not (isinstance(data, list) or isinstance(data, tuple)):
                raise ValueError(ERR_INPUT_NOT_LIST_TUPLE)
            self.data = data
        self.n_elems = len(self.data)

    def __getitem__(self, key=None):
        """
        Returns the element(s) specified by the index/indices in key. Supports
        backwards indexing. If key is None, returns the entire Vactor.
        """
        if isinstance(key, int):
            if key >= 0:
                result = self.data[key]
            else:
                result = self.data[self.n_elems + key]
                
        elif isinstance(key, list) or isinstance(key, tuple):
            result = []
            for k in key:
                if k >= 0:
                    result.append(self.data[k])
                else:
                    result.append(self.data[self.n_elems + k])
        else:
            raise ValueError(ERR_KEY_NOT_INT_LIST_TUPLE)

        return result

    def __str__(self):
        """
        Returns the string representation of the Vector.
        """
        data_str = map(str, self.data)
        output = "["
        output += " ".join([elem for elem in data_str])
        output += "]" 

        return output

    ############################# Unary operators #############################

    def __pos__(self):
        """
        Implements behaviour for unary positive.
        """
        for i in range(self.n_elems):
            self.data[i] = +self.data[i]

    def __neg__(self):
        """
        Implements behaviour for unary negation.
        """
        for i in range(self.n_elems):
            self.data[i] = -self.data[i]

    def __abs__(self):
        """
        Implements behaviour for absolute value (NOT modulus; use dot()).
        """
        for i in range(self.n_elems):                
            self.data[i] = abs(self.data[i])

    # more...

    ############################ Binary operators #############################

    def __add__(self, other):
        """
        Perform element-wise addition of one Vector by another.
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [0.0 for i in range(self.n_elems)]
        for i in range(self.n_elems):
            result[i] = self.data[i] + other.data[i]
        
        return Vector(result)

    def __sub__(self, other):
        """
        Perform element-wise subtraction of one Vector by another.
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
        
        result = [0.0 for i in range(self.n_elems)]
        for i in range(self.n_elems):
            result[i] = self.data[i] - other.data[i]
        
        return Vector(result)

    def __mul__(self, other):
        """
        Perform element-wise multiplication of one Vector by another.
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
                             
        result = [0.0 for i in range(self.n_elems)]
        for i in range(self.n_elems):
            result[i] = self.data[i] * other.data[i]

        return Vector(result)

    def __div__(self, other):
        """
        Perform element-wise division of one Vector by another.
        """
        if not isinstance(other, Vector):
            raise ValueError(ERR_OP_NOT_VEC)
        if not (self.n_elems == other.n_elems):
            raise ValueError(ERR_OP_BAD_DIMS)
                             
        result = [0.0 for i in range(self.n_elems)]
        for i in range(self.n_elems):
            result[i] = float(self.data[i]) / other.data[i]

        return Vector(result)

    def add_scalar(self, value):
        """
        Returns a new Vector with the input value added to every element.
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] += value

        return Vector(result)
    
    def sub_scalar(self, value):
        """
        Returns a new Vector with the input value subtracted from every element.
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] -= value

        return Vector(result)
    
    def mul_scalar(self, value):
        """
        Returns a new Vector with every element multiplied by the input value.
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] *= value

        return Vector(result)
    
    def div_scalar(self, value):
        """
        Returns a new Vector with every element divided by the input value.
        """
        result = self.data[:]
        for i, v in enumerate(result):
            result[i] /= value

        return Vector(result)
        
    def pushback(self, value):
        """
        Adds the input value to the end of the Vector.
        """
        self.data.append(value)
        self.n_elems = len(self.data)

class Matrix(object):
    """
    The generic matrix class.
    """
    def __init__(self, data=None):
        if data == None:
            self.data = []
        else:
            if not (isinstance(data, list) or isinstance(data, tuple)):
                raise ValueError(ERR_INPUT_NOT_LIST_TUPLE)
            self.data = data
        # TODO: raise error if not all rows have same length
        self.n_rows = len(data)
        self.n_cols = len(data[0])
    
    def __getitem__(self):
        """
        DEFINE ME
        """
        return

    def __str__(self):
        """
        Returns the string representation of the Matrix.
        """
        output = "["
        for i in range(self.n_rows):
            row_str = map(str, self.data[i])
            if i != 0:
                output += " "
            output += "["
            output += " ".join([elem for elem in row_str])
            output += "]"
            if i != self.n_rows - 1:
                output += "\n"
        output += "]"
        return output

    def __add__(self, other):
        """
        Perform element-wise addition of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] + other.data[i][j]

        return Matrix(result)

    def __sub__(self, other):
        """
        Perform element-wise subtraction of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] - other.data[i][j]
        
        return Matrix(result)

    def __mul__(self, other):
        """
        Perform element-wise multiplication of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = self.data[i][j] * other.data[i][j]

        return Matrix(result)

    def __div__(self, other):
        """
        Perform element-wise division of one Matrix by another.
        """
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)
        if not (self.n_rows == other.n_rows and self.n_cols == other.n_cols):
            raise ValueError(ERR_OP_BAD_DIMS)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(self.n_cols)]

        for i in range(self.n_rows):
            for j in range(self.n_cols):
                result[i][j] = float(self.data[i][j]) / other.data[i][j]

        return Matrix(result)

    def pushback_row(self, row):
        """
        Adds the input row to the bottom of the Matrix.
        """
        if len(row) != self.n_cols and self.n_rows != 0:
            raise ValueError(ERR_INPUT_BAD_DIMS)
        
        self.data.append(row)
        self.n_rows = len(self.data)

    def pushback_col(self, col):
        """
        Add the input column to the right of the Matrix.
        """
        if len(col) != self.n_rows and self.n_cols != 0:
            raise ValueError(ERR_INPUT_BAD_DIMS)

        for i in range(self.n_rows):
            self.data[i].append(col[i])
        self.n_cols = len(self.data[0])

    def matrix_product(self, other):
        if not isinstance(other, Matrix):
            raise ValueError(ERR_OP_NOT_MAT)

        result = [[0.0 for i in range(self.n_rows)]
                  for j in range(other.n_cols)]

        for i in range(self.n_rows):
            for j in range(other.n_cols):
                result[i][j] = (mathsci.math.linalg.dot_product
                                (self.data[i], zip(*other.data)[j]))

        return Matrix(result)

    def inverse(self):
        return

if __name__ == "__main__":
    A = Matrix([[1, 2], [3, 4]])
    B = Matrix([[5, 6], [7, 8]])

    print A + B
    print A - B
    print A * B
    print A / B
    print A.matrix_product(B)
    print

    c = Vector([1, 2, 3, 4, 5])
    d = Vector([2, 3, 4, 5, 6])

    print c + d
    print c - d
    print c * d
    print c / d

    c.pushback(9)
    print c
    print c[2], c[4], c[-1], c[-3]
    print

    A.pushback_row([9, 0])
    print A
    A.pushback_col([7, 8, 9])
    print A
