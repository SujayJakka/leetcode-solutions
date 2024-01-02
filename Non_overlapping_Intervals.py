class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals = sorted(intervals, key=lambda x: x[0])
        res = 0
        currEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] >= currEnd:
                currEnd = intervals[i][1]
            else:
                res += 1
                currEnd = min(currEnd, intervals[i][1])

        return res
