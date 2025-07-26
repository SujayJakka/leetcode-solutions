class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(i, j):
            if min(i, j) < 0 or i == ROWS or j == COLS or grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res