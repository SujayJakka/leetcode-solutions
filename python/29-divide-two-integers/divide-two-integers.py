class Solution(object):
    def divide(self, dividend, divisor):
        count = 0
        if(dividend == 0):
            return 0
        if(dividend < 0 and divisor > 0):
            dividend = abs(dividend)
            count = self.fakeDivision(dividend, divisor)
            count = -count
        elif(dividend > 0 and divisor < 0):
            divisor = abs(divisor)
            count = self.fakeDivision(dividend, divisor)
            count = -count
        elif(dividend < 0 and divisor < 0):
            divisor = abs(divisor)
            dividend = abs(dividend)
            count = self.fakeDivision(dividend, divisor)
        else:
            count = self.fakeDivision(dividend, divisor)
        
        if(count >= pow(2,31)):
            return pow(2,31) - 1
        if(count < pow(-2,31)):
            return pow(-2,31)
        return count
    
    def fakeDivision(self, dividend, divisor):
        count = dividend // divisor
        return count
        