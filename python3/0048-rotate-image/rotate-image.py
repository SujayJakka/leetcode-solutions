class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l):

                top, bottom = l, r
                
                # Save Top Left Value
                top_left = matrix[top][l + i]

                # Move Bottom Left into Top Left
                matrix[top][l + i] = matrix[bottom - i][l]

                # Move Bottom Right into Bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # Move Top Right into Bottom Right
                matrix[bottom][r - i] = matrix[top + i][r]

                # Move Top Left into Top Right
                matrix[top + i][r] = top_left

            l += 1
            r -= 1