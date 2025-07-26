class Solution:
    def tribonacci(self, n: int) -> int:
        
        cache = {0: 0, 1: 1, 2: 1}
        
        def dfs(i):

            if i in cache:
                return cache[i]
            
            res = dfs(i - 1) + dfs(i - 2) + dfs(i - 3)
            cache[i] = res
            return res
        
        return dfs(n)