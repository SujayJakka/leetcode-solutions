class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr_1, ptr_2 = 0, 0
        res = []
        for i in range(len(word1) + len(word2)):
            if ptr_1 == len(word1):
                res.append(word2[ptr_2:])
                break
            if ptr_2 == len(word2):
                res.append(word1[ptr_1:])
                break
            
            if ptr_1 == ptr_2:
                res.append(word1[ptr_1])
                ptr_1 += 1
            else:
                res.append(word2[ptr_2])
                ptr_2 += 1
        
        return "".join(res)
        