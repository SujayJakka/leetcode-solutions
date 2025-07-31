class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        max_boundary = float("-inf")
        res = 0
        for i in range(len(intervals)):
            if i + 1 < len(intervals) and intervals[i][0] == intervals[i + 1][0]:
                res += 1
            elif intervals[i][1] <= max_boundary:
                res += 1
            max_boundary = max(intervals[i][1], max_boundary)
        return len(intervals) - res

        