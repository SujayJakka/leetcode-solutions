import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        max_heap = []
        
        for i in range(0, len(heights) - 1):

            diff = heights[i + 1] - heights[i]

            if diff < 0:
                continue

            if bricks < diff and ladders == 0:
                return i
            
            # Use Bricks
            if bricks >= diff:
                heapq.heappush(max_heap, -1 * diff)
                bricks = bricks - diff
            # Not enough bricks
            else:
                if max_heap and diff < max_heap[0] * -1:
                    bricks -= diff
                    bricks += (max_heap[0] * -1)
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, -1 * diff)
                ladders -= 1
                
        return len(heights) - 1
        

        

        