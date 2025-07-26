class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        start = sorted([x[0] for x in intervals])
        end = sorted([x[1] for x in intervals])
        
        s = e = 0
        count = res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                count += 1
                s += 1
            else:
                count -= 1
                e += 1
            
            res = max(res, count)
        
        return res