class Solution:
    def countSubstrings(self, s: str) -> int:

        thingSet = set()
        count = 0

        for i in range(len(s)):
            for j in range(i, len(s)):
                cString = s[i:j+1]
                if(cString in thingSet):
                    count += 1
                else:
                    boolThing = self.checkPalindrome(i, j, s)
                    if boolThing:
                        count += 1
                        thingSet.add(cString)
        return count
        
    
    def checkPalindrome(self, l, r, s):

        while(l <= r):
            if(s[l] != s[r]):
                return False
            else:
                l += 1
                r -= 1
        return True
