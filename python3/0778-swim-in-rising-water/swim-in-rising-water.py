import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        visited.add((grid[0][0], 0, 0))
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        min_h = []
        heappush(min_h, (grid[0][0], 0, 0))

        while min_h:
            t, i, j = heappop(min_h)

            if i == n - 1 and j == n - 1:
                return t
            
            for v, h in directions:
                new_i = i + v
                new_j = j + h

                if not ((new_i, new_j) not in visited and 0 <= new_i < n and 0 <= new_j < n):
                    continue
                
                visited.add((new_i, new_j))
                heapq.heappush(min_h, (max(t, grid[new_i][new_j]), new_i, new_j))

        



