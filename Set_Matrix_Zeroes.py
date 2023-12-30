class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def turnAsterick(i, j):
            for row in range(len(matrix)):
                if matrix[row][j] != 0:
                    matrix[row][j] = "*"
            for col in range(len(matrix[0])):
                if matrix[i][col] != 0:
                    matrix[i][col] = "*"
            

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    turnAsterick(i, j)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "*":
                    matrix[i][j] = 0
        
