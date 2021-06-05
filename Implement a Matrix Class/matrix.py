import math
from math import sqrt
import numbers

def zeroes(height, width):
        #"""
        #Creates a matrix of zeroes.
        #"""
        g = [[0.0 for k in range(width)] for l in range(height)]
        for i in range(height):
            for j in range(width):
                g[i][j] = 0
        return Matrix(g)

def identity(n):
        #"""
        #Creates a n x n identity matrix.
        #"""
        I = zeroes(n, n)
        for i in range(n):
            for j in range(n):
                if (i == j):
                    I[i][j] = 1.0
                else:
                    I[i][j] = 0                  
        return I

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
            det = grid[0][0]
        if self.h == 2:
            a = (grid[0][0]*grid[1][1]) - (grid[0][1]*grid[1][0]) 
            det = 1/a
        return Matrix(det)
        # TODO - your code here

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        #if self.h > 2:
            #raise(NotImplementedError, "Calculating trace not implemented for matrices largerer than 2x2.")
        tr = 0.0
        if self.h == 1:
            tr = grid[0][0]
        else:
            for i in range(self.h):
                for j in range(self.w):
                    if i==j:
                        tr +=self.g[i][j]  
        
        return tr
        # TODO - your code here

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        inv = []
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")
        if self.h == 1:
            inv.append ([1 / self.g[0][0]])
        elif self.h == 2:
            if self.g[0][0] * self.g[1][1] == self.g[0][1] * self.g[1][0]:
                raise ValueError('The matrix is not invertible.')
            else:
            # Calculate the inverse of the square 1x1 or 2x2 matrix.
                a = self.g[0][0]
                b = self.g[0][1]
                c = self.g[1][0]
                d = self.g[1][1]

                factor = 1 / (a * d - b * c)

                inv = [[d, -b],[-c, a]]

                for i in range(len(inv)):
                    for j in range(len(inv[0])):
                        inv[i][j] = factor * inv[i][j]
    
        return Matrix(inv)
        # TODO - your code here

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        # TODO - your code here
        matrix_transpose = [[0 for i in range(self.h)] for j in range(self.w)]
    
        for k in range(self.h):
            for l in range(self.w):
                matrix_transpose[l][k] = self.g[k][l]

            
    
        return Matrix(matrix_transpose)
        

    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
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

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        matrixsum = []
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        for i in range(self.h):
            row = []
            for j in range(self.w):
                z = self.g[i][j] + other.g[i][j]
                row.append(z)
            matrixsum.append(row)
        
        return Matrix (matrixsum)
        #   
        # TODO - your code here
        #

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
        neg = []
        for i in range(self.h):
            row =[]
            for j in range(self.w):
                row.append(-1*self.g[i][j])
            neg.append(row)
        return Matrix (neg)
                
        #   
        # TODO - your code here
        #
        

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        matrixsub = []
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
        for i in range(self.h):
            row = []
            for j in range(self.w):
                z = self.g[i][j] - other.g[i][j]
                row.append(z)
            matrixsub.append(row)
        
        return Matrix(matrixsub)
        #   
        # TODO - your code here
        #

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """
        if self.w != other.h:
            raise(ValueError, "These Matrices cannot be multiplied ") 
        
        res = [[0 for x in range(other.w)] for y in range(self.h)] 
  
        # explicit for loops
        for i in range(self.h):
            for j in range(other.w):
                for k in range(other.h):                  
                    res[i][j] = res[i][j] + (self.g[i][k] * other.g[k][j])
        #   
        # TODO - your code here
        #
        return Matrix(res)


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
        prod = [[0 for x in range(self.w)] for y in range(self.h)]
        if isinstance(other, numbers.Number):
            for i in range(self.h):
                for j in range(self.w):
                    prod[i][j] = other * self.g[i][j]
            
            return Matrix(prod)
