class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.prefix_matrix[r][c + 1]
                self.prefix_matrix[r + 1][c + 1] = above + prefix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1, r2 = row1 + 1, row2 + 1
        c1, c2 = col1 + 1, col2 + 1

        above = self.prefix_matrix[r1 - 1][c2]
        left =  self.prefix_matrix[r2][c1 - 1]
        top_left = self.prefix_matrix[r1 - 1][c1 - 1]

        return self.prefix_matrix[r2][c2] - above - left + top_left

        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)