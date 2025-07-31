class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        if len(arr) == 1:
            return [-1]
        
        res = []

        res.append(-1)
        max_number = arr[-1]
        res.append(max_number)
        
        for i in range(len(arr) - 2, 0, -1):
            max_number = max(max_number, arr[i])
            res.append(max_number)
        
        return res[::-1]
