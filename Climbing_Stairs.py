class Solution:
    def climbStairs(self, n: int) -> int:
        var1, var2 = 1,1
        for i in range(1, n):
            temp = var1 + var2
            var2 = var1
            var1 = temp
        return var1
