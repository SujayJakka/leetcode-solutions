class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_min, global_min = nums[0], nums[0]
        curr_max, global_max = nums[0], nums[0]
        total = nums[0]

        for i in range(1, len(nums)):
            curr_min = min(curr_min + nums[i], nums[i])
            curr_max = max(curr_max + nums[i], nums[i])

            global_min = min(global_min, curr_min)
            global_max = max(global_max, curr_max)

            total += nums[i]
        
        return global_max if total - global_min == 0 else max(total - global_min, global_max)

        
            

