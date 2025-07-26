class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        cacheMap = {}


        def dfs(i, canBuy):

            if i >= len(prices):
                return 0

            if (i, canBuy) in cacheMap:
                return cacheMap[(i, canBuy)]
            

            coolDown = dfs(i+1, canBuy)
            
            if canBuy:
                buy = dfs(i+1, not canBuy) - prices[i]
                cacheMap[(i, canBuy)] = max(coolDown, buy)
                        
            else:
                sell = dfs(i+2, not canBuy) + prices[i]
                cacheMap[(i, canBuy)] = max(coolDown, sell)
            
            return cacheMap[(i, canBuy)]
        
        return dfs(0, True)
