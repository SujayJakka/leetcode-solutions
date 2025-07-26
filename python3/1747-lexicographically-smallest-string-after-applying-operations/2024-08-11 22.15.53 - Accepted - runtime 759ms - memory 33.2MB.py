class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        
        cache = set()

        def rotate(curr):
            return curr[-b:] + curr[:-b]
        
        def add(curr):
            new_curr = [""] * len(s)
            for i in range(len(s)):
                if i % 2:
                    new_curr[i] = str((int(curr[i]) + a) % 10)
                else:
                    new_curr[i] = curr[i]

            return "".join(new_curr)
        
        res = [s]

        def dfs(curr):
            if curr in cache:
                return
            
            res[0] = min(res[0], curr)
            cache.add(curr)
            
            rotate_curr = rotate(curr)
            add_curr = add(curr)

            dfs(rotate_curr)
            dfs(add_curr)
            
            return
        
        dfs(s)
        return res[0]
