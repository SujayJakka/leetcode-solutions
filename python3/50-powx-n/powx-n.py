class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        def recursive_method(x, exponent):
            if exponent == 1:
                return x
            
            temp = recursive_method(x, exponent // 2)

            if exponent % 2 == 0:
                return temp * temp
            else:
                return temp * temp * x
        
        res = recursive_method(x, abs(n))
        return 1 / res if n < 0 else res