class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        carry = 1

        for i in range(len(digits) - 1, -1, -1):
            if carry == 0:
                break
            digit = (digits[i] + carry) % 10
            carry = (digits[i] + carry) // 10
            digits[i] = digit
        
        return [1] + digits if carry == 1 else digits
        