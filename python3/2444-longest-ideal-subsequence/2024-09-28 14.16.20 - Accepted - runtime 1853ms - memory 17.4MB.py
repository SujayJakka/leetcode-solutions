class Solution:
    def longestIdealString(self, s: str, k: int) -> int:

        dp = [0] * 26
        
        for c in s:
            index = ord(c) - ord("a")
            prev_c = dp[index]
            for j in range(26):
                if abs(j - index) <= k:
                    if index == j:
                        dp[index] = max(prev_c + 1, dp[index])
                    else:
                        dp[index] = max(dp[index], dp[j] + 1)
        
        return max(dp)

            


            

        