class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if len(digits) == 0:
            return []

        res = []
        h_map = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], 
            "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}

        def recursive_method(count, curr):
            if count == len(digits):
                curr = "".join(curr)
                res.append(curr)
                return

            digit = digits[count]
            digit_numbers = h_map[digit]
            count += 1

            for i in range(len(digit_numbers)):
                curr.append(digit_numbers[i])
                recursive_method(count, curr)
                curr.pop()
        
        recursive_method(0, [])
        return res
