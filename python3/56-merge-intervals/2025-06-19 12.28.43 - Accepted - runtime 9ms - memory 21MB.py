class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        res = [intervals[0]]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            res_start, res_end = res[-1]

            if curr_start <= res_end:
                res.pop()
                res.append([res_start, max(res_end, curr_end)])
            else:
                res.append(intervals[i])


        return res