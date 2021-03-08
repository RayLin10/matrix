"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1   1       1
"""
import math

# Print the matrix such that it looks like
# the template in the top comment
def print_matrix(matrix):
    rows = 4
    cols = len(matrix[0])
    result = ""

    for r in range(rows):
        for c in range(cols):
            result += str(matrix[r][c]) + ' '
        result += '\n'
    print(result)

# Turn the paramter matrix into an identity matrix
# You may assume matrix is square
def ident(matrix):
    size = len(matrix)

    for x in range(size):
        for y in range(size):
            if x == y:
                matrix[x][y] = 1
            else:
                matrix[x][y] = 0

# Multiply m1 by m2, modifying m2 to be the product
# m1 * m2 -> m2
def matrix_mult(m1, m2):
    temp = [x[:] for x in m2]
    size = len(m2[0])

    for x in range(4):
        for y in range(size):
            sum = 0
            for z in range(4):
                sum += m1[x][z] * temp[z][y]
                m2[x][y] = sum 

def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range(cols):
        m.append([])
        for r in range(rows):
            m[c].append(0)
    return m
