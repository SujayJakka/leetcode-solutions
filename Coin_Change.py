class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        minValue = [2**31] * (amount + 1)
        minValue[0] = 0

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    minValue[i] = min(minValue[i], 1 + minValue[i-c])
        
        return minValue[amount] if minValue[amount] != 2**31 else -1
