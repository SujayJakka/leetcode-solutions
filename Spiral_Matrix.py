class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        while matrix:
            res.extend(matrix.pop(0)) # left to right
            if matrix and matrix[0]: # top to down
                for row in matrix:
                    res.append(row.pop())
            if matrix: # right to left
                res.extend(matrix.pop()[::-1])
            if matrix and matrix[0]: # bottom to up
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res
        
