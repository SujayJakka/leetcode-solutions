class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        res = []
        a_ptr, b_ptr, carry = len(a) - 1, len(b) - 1, 0

        while a_ptr >= 0 or b_ptr >= 0 or carry:
            a_val, b_val = 0, 0

            if a_ptr >= 0:
                a_val = int(a[a_ptr])
            
            if b_ptr >= 0:
                b_val = int(b[b_ptr])
            
            curr = a_val ^ b_val ^ carry
            res.append(str(curr))

            if (a_val & b_val) or (a_val & carry) or (b_val & carry):
                carry = 1
            else:
                carry = 0
            
            a_ptr -= 1
            b_ptr -= 1
        
        return "".join(res[::-1])

