import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = sum([x for x, y in costs])
        max_heap = []
        heapify(max_heap)

        for x, y in costs:
            heappush(max_heap, y - x)
        
        for i in range(len(costs) // 2):
            res += heappop(max_heap)
        
        return res
        
