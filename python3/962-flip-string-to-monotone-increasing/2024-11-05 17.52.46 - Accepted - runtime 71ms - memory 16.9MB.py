class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        res = 0
        num_ones = 0
        for i in range(len(s)):
            if s[i] == "1":
                num_ones += 1
            else:
                res = min(num_ones, res + 1)
        
        return res


        