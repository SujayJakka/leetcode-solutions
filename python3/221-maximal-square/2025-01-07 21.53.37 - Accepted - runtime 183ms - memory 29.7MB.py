class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i in range(len(matrix[0])):
            res = max(int(matrix[-1][i]), res)
        for i in range(len(matrix)):
            res = max(int(matrix[i][-1]), res)
            
        for i in range(len(matrix) - 2, -1, -1):
            for j in range(len(matrix[0]) - 2, -1, -1):
                min_value = min(int(matrix[i + 1][j]), int(matrix[i][j + 1]), int(matrix[i + 1][j + 1]))
                if matrix[i][j] == "1":
                    matrix[i][j] = min_value + 1
                    res = max(res, matrix[i][j])
        
        return res**2


        