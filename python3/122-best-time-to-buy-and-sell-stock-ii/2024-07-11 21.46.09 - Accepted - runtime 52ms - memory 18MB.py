class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0
        curr_price = prices[0]

        for i in range(1, len(prices)):
            if curr_price < prices[i]:
                res += prices[i] - curr_price
            curr_price = prices[i]

        return res

        