class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        res = 1
        intervals = sorted(intervals, key=lambda x: x[0])
        meetingRooms = [intervals[0]]

        for start, end in intervals[1:]:
            thing = 0
            for i in range(len(meetingRooms)):
                if start >= meetingRooms[i][1]:
                    thing = 1
                    meetingRooms.pop(i)
                    meetingRooms.append([start, end])
                    break
            if(thing == 0):
                res += 1
                meetingRooms.append([start, end])

        return res
            
            


        
