class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        carry = 0
        res = 0

        mask = 0xFFFFFFFF

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1

            res_bit = a_bit ^ b_bit ^ carry
            carry = a_bit + b_bit + carry >= 2

            if res_bit:
                res = res | (1 << i)
        
        if res > 0x7FFFFFFF:
            res = ~(res ^ mask)
        
        return res

