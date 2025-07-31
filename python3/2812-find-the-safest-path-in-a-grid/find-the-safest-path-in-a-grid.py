import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])

        distance_from_thieves = {}
        queue = Deque()
        visit = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    visit.add((r, c))
        
        distance = 0
        
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                distance_from_thieves[(r, c)] = distance

                directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

                for new_r, new_c in directions:
                    if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                        if (new_r, new_c) not in visit:
                            queue.append((new_r, new_c))
                            visit.add((new_r, new_c))
            
            distance += 1
        

        for r, c in distance_from_thieves:
            grid[r][c] = distance_from_thieves[(r, c)]


        max_heap = []
        visit = set()

        heapq.heappush(max_heap, (-grid[0][0], 0, 0))

        while max_heap:
            val, r, c = heapq.heappop(max_heap)
            val *= -1

            if r == ROWS - 1 and c == COLS - 1:
                return val
            
            if (r, c) in visit:
                continue
            
            visit.add((r, c))

            directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for new_r, new_c in directions:
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    if (new_r, new_c) not in visit:
                        heapq.heappush(max_heap, (-1 * min(val, grid[new_r][new_c]), new_r, new_c))
        