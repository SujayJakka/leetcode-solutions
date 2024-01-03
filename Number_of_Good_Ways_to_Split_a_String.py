class Solution:
    def numSplits(self, s: str) -> int:
        left = Counter()
        right = Counter(s)
        result = 0
        for c in s:
            left[c]+=1
            right[c]-=1
            if(right[c] == 0):
                del right[c]
            if(len(left) == len(right)):
                result+=1
        return result
