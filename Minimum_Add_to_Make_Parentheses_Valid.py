class Solution:
    def minAddToMakeValid(self, s: str) -> int:

        stack = []

        for i in range(len(s)):
            if s[i] == "(":
                stack.append("(")
            else:
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(")")


        return len(stack)
