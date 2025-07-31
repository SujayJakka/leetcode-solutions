import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res, i = {}, 0
        min_heap = []

        for query in sorted(queries):
            while i < len(intervals) and query >= intervals[i][0]:
                heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            
            while min_heap and min_heap[0][1] < query:
                heappop(min_heap)
            
            res[query] = min_heap[0][0] if min_heap else -1

        return [res[query] for query in queries]