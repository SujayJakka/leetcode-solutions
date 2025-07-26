class Solution:
    def splitString(self, s: str) -> bool:

        def backtrack(i, prev):
            if i == len(s):
                return True

            for j in range(i, len(s)):
                if int(s[i: j + 1]) + 1 == prev and backtrack(j + 1, int(s[i: j + 1])):
                    return True
            return False
        
        for i in range(len(s) - 1):
            if backtrack(i + 1, int(s[:i + 1])):
                return True
        return False

            
        