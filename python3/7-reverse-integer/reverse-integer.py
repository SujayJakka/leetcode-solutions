class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2**31 - 1
        MIN = -2**31

        res = 0
        
        while x != 0:
            mod_integer = int(math.fmod(x, 10)) 
            x = int(x / 10)

            if res > MAX // 10 or (res == MAX // 10 and mod_integer > 7):
                return 0
            
            if res < MIN // 10 or (res == MIN // 10 and mod_integer < 8):
                return 0
            
            res = (res * 10) + mod_integer
        
        return res
        
