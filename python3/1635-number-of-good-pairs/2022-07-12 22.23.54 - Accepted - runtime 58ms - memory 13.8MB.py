class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        for x in range(0, len(nums) - 1):
            for y in range(x + 1, len(nums)):
                if(nums[x] == nums[y]):
                    result+=1
        return result
                    
            
        