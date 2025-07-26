class Solution:
    def numDecodings(self, s: str) -> int:
        # arr = [0] * (len(s) + 1)
        # arr[-1] = 1

        # for i in range(len(s)-1, -1, -1):
        #     if s[i] == "0":
        #         continue
            
        #     arr[i] += arr[i+1]

        #     if i + 1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
        #         arr[i] += arr[i+2]

        # return arr[0]

        dp = {len(s):1}

        def dfs(i):
            if i in dp:
                return dp[i]
            elif s[i] == "0":
                dp[i] = 0
                return 0
            
            dp[i] = dfs(i+1)

            if i + 1 < len(s) and 1 <= int(s[i:i+2]) <= 26:
                dp[i] += dfs(i+2)
            
            return dp[i]
        
        return dfs(0)
        