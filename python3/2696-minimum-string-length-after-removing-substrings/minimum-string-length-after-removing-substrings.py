class Solution:
    def minLength(self, s: str) -> int:
        stack = [] 
        stack.append(s[0])

        for i in range(1, len(s)):
            if stack:
                sub = stack[-1] + s[i]
                if sub == "AB" or sub == "CD":
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
        
        return len(stack)