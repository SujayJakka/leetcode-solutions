import heapq

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips = sorted(trips, key=lambda x: x[1])
        min_heap = []
        total_passengers = 0

        for i in range(len(trips)):
            passengers, start, end = trips[i]
            while min_heap and min_heap[0][0] <= start:
                prev_end, prev_passengers = heapq.heappop(min_heap)
                total_passengers -= prev_passengers
        
            total_passengers += passengers
            if total_passengers > capacity:
                return False
            heapq.heappush(min_heap, (end, passengers))
        
        return True

