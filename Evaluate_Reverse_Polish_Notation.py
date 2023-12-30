class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+" or token == "-" or token == "/" or token == "*":
                num2 = stack.pop()
                num1 = stack.pop()

                if token == "+":
                    num3 = num1 + num2
                
                elif token == "-":
                    num3 = num1 - num2
                
                elif token == "/":
                    num3 = num1 / num2
                
                elif token == "*":
                    num3 = num1 * num2
                
                stack.append(int(num3))

            else:
                stack.append(int(token))

        return stack.pop()
