class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            if i == len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            
            if j + 1 < len(p) and p[j + 1] == "*":
                dp[(i, j)] = (match and dfs(i + 1, j)) or (dfs(i, j + 2))
                return dp[(i, j)]
            
            if match:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]

            dp[(i, j)] = False
            return dp[(i, j)]

        return dfs(0, 0)