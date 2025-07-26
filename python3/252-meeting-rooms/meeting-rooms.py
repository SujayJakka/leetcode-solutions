class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        intervals = sorted(intervals)

        if not intervals:
            return True

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if prev_end > start:
                return False
            
            prev_end = end
        
        return True