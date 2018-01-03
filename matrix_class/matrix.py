import math
from math import sqrt
import numbers


def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)


def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I


def dot_product(v1, v2):
    return sum([v1[k] * v2[k] for k in range(len(v1))])


class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        if self.h == 1:
            return self.g[0][0]
        else:
            return self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0]

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        return sum([self.g[k][k] for k in range(self.h)])

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise (ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise (NotImplementedError, "Inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            return Matrix([[1.0/self.g[0][0]]])
        else:
            det = self.determinant()
            if det == 0:
                raise (ValueError, "The determinant of this matrix is zero, so it is not invertible.")
                return None
            else:
                inverse = (1.0/det)*Matrix([[ self.g[1][1], -self.g[0][1]],
                                            [-self.g[1][0],  self.g[0][0]]])
        return inverse

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        transpose = []
        for j in range(self.w):
            new_row = []
            for i in range(self.h):
                new_row.append(self.g[i][j])
            transpose.append(new_row)
        return Matrix(transpose)

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self, idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self, other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same.") 
        matrixSum = []
        for i in range(self.h):
            row = [self.g[i][k] + other.g[i][k] for k in range(self.w)]
            matrixSum.append(row)
        return Matrix(matrixSum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        negation = []
        for row in self.g:
            new_row = [-row[k] for k in range(self.w)]
            negation.append(new_row)
        return Matrix(negation)

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        return self + (-other)
        
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        otherT = other.T()
        product = []
        for rA in self.g:
            new_row = []
            for rB in otherT.g:
                dp = dot_product(rA, rB)
                new_row.append(dp)
            product.append(new_row)
        return Matrix(product)

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            product = []
            for row in self.g:
                new_row = [row[k]*other for k in range(self.w)]
                product.append(new_row)
            return Matrix(product)
