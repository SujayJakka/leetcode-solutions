class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        dp = {len(s):True}
        
        def dfs(start):
            if start in dp:
                return dp[start]
            elif s[start:] in wordDict:
                dp[start] = True
                return True
            
            for i in range(start, len(s)):
                if s[start:i+1] in wordDict:
                    if dfs(i + 1):
                        dp[start] = True
                        return True
            
            dp[start] = False
            return False

        return dfs(0)