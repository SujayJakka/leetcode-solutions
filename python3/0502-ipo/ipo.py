class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        min_heap = [(c, p) for c, p in zip(capital, profits)]
        heapify(min_heap)

        max_heap = []

        for _ in range(k):

            while min_heap and min_heap[0][0] <= w:
                heappush(max_heap, -heappop(min_heap)[1])
            
            if not max_heap:
                break
            
            w += -heappop(max_heap)
        
        return w

        