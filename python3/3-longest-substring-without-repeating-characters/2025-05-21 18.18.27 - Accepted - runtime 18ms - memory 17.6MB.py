class Solution:
    def lengthOfLongestSubstring(self, s):

        my_set = set()
        l, r = 0, 0
        res = 0

        while r < len(s):


            while s[r] in my_set:
                my_set.remove(s[l])
                l += 1
            
            my_set.add(s[r])
            res = max(res, r - l + 1)
            
            r += 1
        
        return res
        
        
        


        