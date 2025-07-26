import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        min_heap = []
        ROWS, COLS = len(heights), len(heights[0])
        visit = set()
        heappush(min_heap, (0, 0, 0))

        while min_heap:
            diff, r, c = heappop(min_heap)
            if r == ROWS - 1 and c == COLS - 1:
                return diff
            
            if (r, c) in visit:
                continue
                
            visit.add((r, c))
            val = heights[r][c]
            directions = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for new_r, new_c in directions:
                if 0 <= new_r < ROWS and 0 <= new_c < COLS:
                    if (new_r, new_c) not in visit:
                        new_diff = abs(heights[new_r][new_c] - val)
                        heappush(min_heap, (max(new_diff, diff), new_r, new_c))
            



        