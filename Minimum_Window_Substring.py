class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "": return ""
        
        windowMap, alphaFreq = {}, {}

        for c in t:
            alphaFreq[c] = 1 + alphaFreq.get(c, 0)
        
        l = 0
        res, beg, end = float("inf"), 1, 0
        have, need = 0, len(alphaFreq)

        for r in range(len(s)):

            windowMap[s[r]] = 1 + windowMap.get(s[r], 0)

            if s[r]in alphaFreq and windowMap[s[r]] == alphaFreq[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < res:
                    res = r - l + 1
                    beg = l
                    end = r
                windowMap[s[l]] -= 1
                if s[l] in alphaFreq and windowMap[s[l]] < alphaFreq[s[l]]:
                    have -= 1
                l+=1
        
        return s[beg:end+1] if res != float("inf") else ""
