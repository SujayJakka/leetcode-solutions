class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = {}
        res = []

        for i in range(len(s)):
            if s[i] not in intervals:
                intervals[s[i]] = [i, i]
            else:
                intervals[s[i]][1] = i
        
        array = list(intervals.values())

        current_interval = array[0]

        for i in range(1, len(array)):
            interval = array[i]

            if interval[0] < current_interval[1]:
                current_interval[0] = min(interval[0], current_interval[0])
                current_interval[1] = max(interval[1], current_interval[1])
            else:
                length = current_interval[1] - current_interval[0] + 1
                res.append(length)
                current_interval = interval
        
        length = current_interval[1] - current_interval[0] + 1
        res.append(length)

        return res

        