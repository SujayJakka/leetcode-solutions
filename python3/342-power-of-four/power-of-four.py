class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        if n == 1:
            return True

        elif n % 4 != 0:
            return False
        else:
            while n >= 4:
                n /= 4
            
            if n == 1:
                return True
            else:
                return False
        