class Solution:
    def getSum(self, a: int, b: int) -> int:

        if(a == 0):
            return b
        
        elif b == 0:
            return a
        
        mask = 0xffffffff

        while b != 0:
            temp = a
            a = (a ^ b) & mask 
            b = ((temp & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
