class Solution:
    def kthCharacter(self, k: int) -> str:

        res = 0

        while k != 1:
            t = floor(math.log2(k))

            if k == (2 ** t):
                k = k - (2 ** (t - 1))
            else:
                k = k - (2 ** t)
            
            res += 1
        
        return chr(ord("a") + res)
        