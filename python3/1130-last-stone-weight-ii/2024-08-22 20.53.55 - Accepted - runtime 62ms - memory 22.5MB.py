class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stone_sum = sum(stones)
        target = ceil(stone_sum / 2)
        cache = {}

        def dfs(i, total):
            if total >= target or i == len(stones):
                return (abs(total - (stone_sum - total)))
            
            if (i, total) in cache:
                return cache[(i, total)]
            
            cache[(i, total)] = min(dfs(i + 1, total + stones[i]), dfs(i + 1, total))
            return cache[(i, total)]

        return dfs(0, 0)

        
        