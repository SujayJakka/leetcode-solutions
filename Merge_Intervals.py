class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        
        intervals = sorted(intervals, key=lambda x: x[0])

        res = [intervals[0]]

        for i in range(1, len(intervals)):

            if res[-1][1] >= intervals[i][0]:
                newInterval = [res[-1][0], max(res[-1][1], intervals[i][1])]
                res[-1] = newInterval
            else: 
                res.append(intervals[i])
        
        return res

