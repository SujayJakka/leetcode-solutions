class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needleSize = len(needle)
        if needle in haystack:
            for i in range(0, len(haystack)):
                if(needle == haystack[i:i+len(needle)]):
                    return i;
                
        elif needle not in haystack:
            return -1
        else:
            return 0
