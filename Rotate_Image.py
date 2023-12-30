class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        queue = []
        flipped = []

        for i in range(len(matrix)):

            for j in range(len(matrix)):

                if i == j or (i,j) in flipped:
                    continue
                else:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
                    flipped.append((i,j))
                    flipped.append((j,i))
        
        l = 0
        r = len(matrix) - 1

        while l < r:
            for i in range(len(matrix)):
                temp = matrix[i][l]
                matrix[i][l] = matrix[i][r]
                matrix[i][r] = temp
            
            l += 1
            r -= 1
        
