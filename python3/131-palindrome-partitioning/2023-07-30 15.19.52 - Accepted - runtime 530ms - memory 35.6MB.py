class Solution:
    def partition(self, s: str) -> List[List[str]]:

        setThing = set()

        res = []

        def isPalindrome(word):

            if word in setThing:
                return True

            l, r = 0, len(word) - 1

            while(l < r):
                if word[l] != word[r]:
                    return False
                
                l += 1
                r -= 1
            
            setThing.add(word)

            return True
        

        def algoThing(l, r, arr):

            if r == len(s):
                return

            while(r < len(s)):
                if isPalindrome(s[l:r+1]):
                    algoThing(l, r+1, arr.copy())
                    arr.append(s[l:r+1])
                    l = r + 1
                    r = l 
                else:
                    r += 1

                    if r == len(s):
                        return

            res.append(arr)
        

        algoThing(0, 0, [])

        return res