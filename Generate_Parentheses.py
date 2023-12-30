class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursive_method(count_OP, count_CP, curr):

            if count_OP == 0:
                for i in range(count_CP):
                    curr += ")"
                res.append(curr)
                return

            if count_CP > count_OP:
                recursive_method(count_OP, count_CP - 1, curr + ")")
            
            recursive_method(count_OP - 1, count_CP, curr + "(")

        recursive_method(n, n, "")

        return res
