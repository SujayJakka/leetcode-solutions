import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        min_heap = []
        h_map = defaultdict(int)
        for num in nums:
            h_map[num] += 1
        
        for key, value in h_map.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap) > k:
                heappop(min_heap)
        
        res = []
        while min_heap:
            value, key = heappop(min_heap)
            res.append(key)
        
        return res