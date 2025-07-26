class Solution:
    def longestPalindrome(self, s: str) -> str:

        table = [[False] * len(s) for _ in range(len(s))]
        res = ""
        res_len = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or table[i+1][j-1]):
                    table[i][j] = True
                    if j - i + 1 > res_len:
                        res_len = j - i + 1
                        res = s[i:j+1]
        return res



        