class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        res = 0

        while k != 1:
            t = floor(log2(k))
            
            if k == 2 ** t:
                k -= (2 ** (t-1))
                t -= 1
            else:
                k -= (2 ** t)

            if operations[t]:
                res += 1

        return chr((res % 26) + ord("a"))
