class Solution:
    def countHillValley(self, nums: List[int]) -> int:

        res = 0

        for i in range(1, len(nums) - 1):
            
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
                continue
            
            if nums[i-1] > nums[i] < nums[i+1] or nums[i-1] < nums[i] > nums[i+1]:
                res += 1

        return res
