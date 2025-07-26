class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        visited = set()

        res = 0

        def dfs(i, j):
            if not (0 <= i < m and 0 <= j < n and (i, j) not in visited and grid[i][j] == 1):
                return 0
            else:
                visited.add((i, j))
                return (1 + dfs(i+1, j) + dfs(i, j+1) + dfs(i-1, j) + dfs(i, j-1))
            
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    res = max(res , dfs(i, j))
        
        return res
            