class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        dfs_cache = {}
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])

        def dfs(i, j):
            if i == ROWS or j == COLS or obstacleGrid[i][j] == 1:
                return 0
            
            if i == ROWS - 1 and j == COLS - 1:
                return 1

            if (i, j) in dfs_cache:
                return dfs_cache[(i, j)]
            
            dfs_cache[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return dfs_cache[(i, j)]
        
        return dfs(0, 0)
            

        