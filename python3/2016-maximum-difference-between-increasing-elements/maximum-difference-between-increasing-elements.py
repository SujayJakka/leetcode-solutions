class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        res = -1
        prefix_min, res = nums[0], -1

        for i in range(1, len(nums)):
            if nums[i] > prefix_min:
                res = max(res, nums[i] - prefix_min)
            else:
                prefix_min = nums[i]

        return res