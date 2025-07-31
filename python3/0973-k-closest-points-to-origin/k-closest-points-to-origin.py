import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x,y in points:
            distance = (x**2 + y**2) ** (1/2)
            minHeap.append([distance, x, y])
        heapq.heapify(minHeap)
        res = []
        for _ in range(k):
            dist, x, y = heapq.heappop(minHeap)
            res.append([x,y])
        return res