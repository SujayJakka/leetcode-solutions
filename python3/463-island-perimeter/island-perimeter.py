class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if  i < 0 or i == len(grid) or j < 0 or j == len(grid[0]) or grid[i][j] == 0:
                return 1
            
            visited.add((i, j))
            arr = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            res = 0
            for x, y in arr:
                if (x, y) in visited:
                    continue
                res += dfs(x, y)
            
            return res
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        