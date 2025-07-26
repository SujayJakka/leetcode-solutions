class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        res = 0

        l, r = 0, 1

        while r < len(prices):

            if prices[r] <= prices[l]:
                l = r
                r = l + 1
                continue

            res = max(res, prices[r] - prices[l])
            r += 1

        
        return res



                
        