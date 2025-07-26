import heapq

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        my_dict = defaultdict(int)
        for num in arr:
            my_dict[num] += 1
        
        min_heap = [my_dict[key] for key in my_dict]
        heapq.heapify(min_heap)

        for _ in range(k):
            min_heap[0] -= 1
            if min_heap[0] == 0:
                heapq.heappop(min_heap)
        
        return len(min_heap)