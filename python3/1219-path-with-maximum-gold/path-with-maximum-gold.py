class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:

        visited = set()

        def dfs(i, j):
            if i < 0 or i == len(grid) or j < 0 or j == len(grid[0]):
                return 0
            
            if grid[i][j] == 0:
                return 0

            directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            res = 0
            for direction in directions:
                if direction not in visited:
                    visited.add(direction)
                    res = max(dfs(direction[0], direction[1]), res)
                    visited.remove(direction)

            return res + grid[i][j]

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                visited.add((i, j))
                res = max(dfs(i, j), res)
                visited.remove((i, j))
        return res
        