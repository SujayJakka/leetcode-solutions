import heapq
from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        
        nums.sort()
        res = 0
        operations = 0

        for i in range(0, len(nums) - 1):
            if nums[i] != nums[i + 1]:
                operations += 1
            res += operations

        return res
        
            

        
        

        