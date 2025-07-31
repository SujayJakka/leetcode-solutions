class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0
        
        nums = sorted(nums)
        l, r = 0, k - 1
        min_value = float("inf")

        while r < len(nums):
            min_value = min(min_value, nums[r] - nums[l])
            l += 1
            r += 1
        
        return min_value


         