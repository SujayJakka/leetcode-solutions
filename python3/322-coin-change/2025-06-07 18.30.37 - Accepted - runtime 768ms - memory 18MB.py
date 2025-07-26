class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = {0:0}

        # def dfs(amount):
        #     if amount in dp:
        #         return dp[amount]
            
        #     total = 1e9

        #     for c in coins:
        #         if amount - c >= 0:
        #             total = min(total, dfs(amount - c) + 1)
            
        #     dp[amount] = total
        #     return dp[amount]

        # min_coins = dfs(amount)
        # return -1 if min_coins == 1e9 else min_coins


        dp_arr = [amount + 1] * (amount + 1)
        dp_arr[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp_arr[i] = min(dp_arr[i-c] + 1, dp_arr[i])
        
        return -1 if dp_arr[amount] == amount + 1 else dp_arr[amount]
            