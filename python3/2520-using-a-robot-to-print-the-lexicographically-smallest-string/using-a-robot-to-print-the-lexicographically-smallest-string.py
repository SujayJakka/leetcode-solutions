class Solution:
    def robotWithString(self, s: str) -> str:

        counter = Counter(s)
        stack = []
        res = []
        remaining_char = "a"

        for c in s:
            stack.append(c)
            counter[c] -= 1

            while remaining_char != "z" and counter[remaining_char] == 0:
                remaining_char = chr(ord(remaining_char)+1)
            
            while stack and stack[-1] <= remaining_char:
                res.append(stack.pop())
        
        return "".join(res)



    



        