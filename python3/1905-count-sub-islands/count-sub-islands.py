class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:

        visited = set()
        
        def dfs(i, j):
            if i < 0 or i == len(grid2) or j < 0 or j == len(grid2[0]) or grid2[i][j] == 0:
                return True
            
            visited.add((i, j))
            res = True

            if grid1[i][j] == 0:
                res = False
            
            arr = [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]
            for x, y in arr:
                if (x, y) not in visited:
                    res = dfs(x, y) and res
            
            return res
        
        res = 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if (i, j) not in visited and grid2[i][j] == 1:
                    if dfs(i, j):
                        res += 1
        return res
        