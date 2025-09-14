class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        
        res = 0
        visited = set()
        queue = Deque()

        def bfs(i, j):

            num_fish = 0
            directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            queue.append((i, j))
            visited.add((i, j))

            while queue:
                r, c = queue.popleft()
                num_fish += grid[r][c]

                for d_r, d_c in directions:
                    if (r + d_r, c + d_c) not in visited and 0 <= r + d_r < len(grid) and 0 <= c + d_c < len(grid[0]) and grid[r + d_r][c + d_c] > 0:
                        visited.add((r + d_r, c + d_c))
                        queue.append((r + d_r, c + d_c))

            return num_fish

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) not in visited and grid[i][j] > 0:
                    res = max(res, bfs(i, j))

        return res
