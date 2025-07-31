class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        visited = {}
        res = 1
        n, m = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(i, j):
            value = 0
            for v,c in directions:
                new_i, new_j = i + v, j + c

                if not(0 <= new_i < n and 0 <= new_j < m and matrix[new_i][new_j] > matrix[i][j]):
                    continue

                if (new_i, new_j) in visited:
                    value = max(value, visited[(new_i, new_j)])
                else:
                    value = max(value, dfs(new_i, new_j))    

            visited[(i, j)] = value + 1
            return visited[(i, j)]

        for i in range(n):
            for j in range(m):
                if (i, j) in visited:
                    continue
                else:
                    value = dfs(i, j)
                    res = max(res, value)
        return res