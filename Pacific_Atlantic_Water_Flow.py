class Solution:

    def __init__(self) -> None:
        self.pacificOcean = False
        self.atlanticOcean = False

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        res = []
    
        def dfs(value, i, j):
            if i < 0 or j < 0:
                self.pacificOcean = True
                return
            
            if i == len(heights) or j == len(heights[0]):
                self.atlanticOcean = True
                return 
            
            if value < heights[i][j] or heights[i][j] == -1:
                return

            if [i,j] in res:
                self.pacificOcean = True
                self.atlanticOcean = True
                return
            
            value = heights[i][j]

            original = heights[i][j]
            heights[i][j] = -1
            dfs(value, i-1, j)
            if self.pacificOcean and self.atlanticOcean:  
                heights[i][j] = original 
                return 
            dfs(value, i, j-1)
            if self.pacificOcean and self.atlanticOcean:  
                heights[i][j] = original 
                return 
            dfs(value, i+1, j)
            if self.pacificOcean and self.atlanticOcean:  
                heights[i][j] = original 
                return
            dfs(value, i, j+1)
            heights[i][j] = original
            return

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                dfs(heights[i][j], i, j)
                if self.pacificOcean and self.atlanticOcean:
                    res.append([i, j])
                self.pacificOcean = False
                self.atlanticOcean = False
        return res
