class Solution:
    def countSubstrings(self, s: str) -> int:
        table = [[False] * len(s) for _ in range(len(s))]
        res = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i <= 2 or table[i+1][j-1]:
                        res += 1
                        table[i][j] = True
    
        return res
            


                
