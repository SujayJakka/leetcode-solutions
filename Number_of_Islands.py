class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def bfs(r,c):
            visited.add((r,c))
            q = collections.deque()
            q.append((r,c))
            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0],[0,1], [0,-1]]
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if(row in range(rows) and col in range(cols) and (row,col) not in visited and grid[row][col] == "1"):
                        q.append((row,col))
                        visited.add((row,col))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1
        return islands
