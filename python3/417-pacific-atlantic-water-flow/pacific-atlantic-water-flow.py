class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(i, j, prev_height, ocean_set):

            if min(i, j) < 0 or i == ROWS or j == COLS or (i, j) in ocean_set or heights[i][j] < prev_height:
                return

            ocean_set.add((i, j))
            dfs(i + 1, j, heights[i][j], ocean_set)
            dfs(i - 1, j, heights[i][j], ocean_set)
            dfs(i, j + 1, heights[i][j], ocean_set)
            dfs(i, j - 1, heights[i][j], ocean_set)
        
        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS - 1, c, heights[ROWS-1][c], atl)
        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS - 1, heights[r][COLS-1], atl)

        
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])

        return res
        