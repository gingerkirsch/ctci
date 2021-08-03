"""
1.8 Zero Matrix: Write an algorithm such that if an element in an M x N matrix is 0,
its entire row and colum are set to 0
"""

ddef setZeroes(matrix):
        n = len(matrix[0])
        m = len(matrix)
        zero_row = False
        zero_col = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        zero_row = True
                    if j == 0:
                        zero_col = True
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if zero_col:
            for i in range(m):
                matrix[i][0] = 0

        if zero_row:
            for j in range(n):
                matrix[0][j] = 0

        return matrix

matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(matrix)
setZeroes(matrix)
print(matrix)
