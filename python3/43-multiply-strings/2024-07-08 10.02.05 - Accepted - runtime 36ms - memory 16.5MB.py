class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        h_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
        h_map_reverse = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}
        num_1_int, num_2_int = 0, 0
        res = []

        for i, c in enumerate(num1):
            integer = h_map[c]
            num_1_int += (pow(10, len(num1) - 1 - i) * integer)
        
        for i, c in enumerate(num2):
            integer = h_map[c]
            num_2_int += (pow(10, len(num2) - 1 - i) * integer)
        
        prod = num_1_int * num_2_int

        while prod != 0:
            res.append(h_map_reverse[prod % 10])
            prod = prod // 10
        
        return "".join(res)[::-1]