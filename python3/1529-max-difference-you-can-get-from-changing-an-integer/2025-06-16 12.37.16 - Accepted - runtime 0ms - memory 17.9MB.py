class Solution:
    def maxDiff(self, num: int) -> int:
        
        num_1 = num_2 = str(num)

        index = 0

        while index < len(num_1) and num_1[index] == "9":
            index += 1
        
        if index < len(num_1):
            num_1 = num_1.replace(num_1[index], "9")
        
        if num_2[0] == "1":
            index = 1
            while index < len(num_2) and (num_2[index] == "1" or num_2[index] == "0"):
                index += 1
            
            if index < len(num_2):
                num_2 = num_2.replace(num_2[index], "0")
        else:
            num_2 = num_2.replace(num_2[0], "1")
        
        return int(num_1) - int(num_2)