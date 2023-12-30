class Solution:
    def numDecodings(self, s: str) -> int:
        dictThing = {len(s):1}

        def algo(i):
            if i in dictThing:
                return dictThing[i]
            if s[i] == "0":
                return 0

            res = algo(i+1)

            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                res += algo(i+2)
            

            dictThing[i] = res
            return res

        return algo(0)


        
