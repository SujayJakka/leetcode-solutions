import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-x for x in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            stone_1 = heappop(max_heap)
            stone_2 = heappop(max_heap)

            if stone_1 == stone_2:
                continue
            
            heappush(max_heap, stone_1 - stone_2)
        
        return 0 if len(max_heap) == 0 else -max_heap[0]