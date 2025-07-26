class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        h_map = {")":"(", "}":"{", "]":"["}


        for c in s:
            if c not in h_map:
                stack.append(c)
            else:
                if not stack or h_map[c] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        return True if not stack else False
