class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def helper(curr_s, target):
            stack = []
            
            for c in curr_s:
                if c == target[1] and stack and stack[-1] == target[0]:
                    stack.pop()
                else:
                    stack.append(c)

            return stack
        

        s = list(s)
        score = 0
        high_substring = "ba" if y > x else "ab"
        low_substring = "ab" if high_substring == "ba" else "ba"

        s_first_pass = helper(s, high_substring)
        score += ((len(s) - len(s_first_pass)) // 2 * max(x, y))

        s_second_pass = helper(s_first_pass, low_substring)
        score += ((len(s_first_pass) - len(s_second_pass)) // 2 * min(x, y))

        return score



            



