class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        mapThing = []

        def algo(s):

            if s in mapThing:
                return False

            if s == "":
                return True
            
            l = 0
            
            for i in range(len(s)):
                word = s[l:i+1]
                if word in wordDict:
                    boolThing = algo(s[i+1:])
                    if boolThing:
                        return True
            
            mapThing.append(s)

            return False
        
        return algo(s)
            
