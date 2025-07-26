class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def dfs(arr, i):

            if len(arr) == k:
                res.append(arr.copy())
                return
            
            if i > n:
                return

            arr.append(i)
            dfs(arr, i + 1)
            arr.pop()
            dfs(arr, i + 1)
        
        dfs([], 1)
        return res