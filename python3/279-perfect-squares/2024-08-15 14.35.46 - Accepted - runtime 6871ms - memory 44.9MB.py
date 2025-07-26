class Solution:
    def numSquares(self, n: int) -> int:
        # limit = int(math.sqrt(n))
        # dp = {}
        # dp[0] = 0

        # for i in range(1, n + 1):
        #     dp[i] = float("inf")
        #     for j in range(1, limit + 1):
        #         dp[i] = min(dp[i], 1 + dp.get(i - (j ** 2), float("inf")))
        # return dp[n]

        dp = {}
        limit = int(math.sqrt(n))

        def dfs(curr):
            if curr == n:
                return 0
            if curr > n:
                return float("inf")
            if curr in dp:
                return dp[curr]
            

            res = float("inf")
            for i in range(1, limit + 1):
                res = min(res, 1 + dfs(curr + (i) ** 2))
            
            dp[curr] = res
            return res

        return dfs(0)