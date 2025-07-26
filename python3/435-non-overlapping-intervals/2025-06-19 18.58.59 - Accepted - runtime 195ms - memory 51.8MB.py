class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        res = 0
        intervals = sorted(intervals)

        current_interval = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] < current_interval[1]:
                res += 1
                current_interval[1] = min(intervals[i][1], current_interval[1])
            else:
                current_interval = intervals[i]

        return res