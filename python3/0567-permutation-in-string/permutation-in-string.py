from collections import deque


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s2) < len(s1):
            return False

        dict_thing = {}
        curr_thing = {}

        for i in range(len(s1)):
            dict_thing[s1[i]] = dict_thing.get(s1[i], 0) + 1

        for i in range(len(s1)):
            curr_thing[s2[i]] = curr_thing.get(s2[i], 0) + 1

        l, r = 0, len(s1) - 1

        while(r < len(s2)):

            if curr_thing == dict_thing:
                return True
            
            else:

                if curr_thing[s2[l]] == 1:
                    curr_thing.pop(s2[l])
                else:
                    curr_thing[s2[l]] -= 1
                
                l += 1
                r += 1

                if r >= len(s2):
                    return False
                
                curr_thing[s2[r]] = curr_thing.get(s2[r], 0) + 1
        
        return False

        