class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        nums = sorted(nums)
        res = 1
        
        min_num = nums[0]

        for num in nums:
            if num - min_num > k:
                res += 1
                min_num = num
        
        return res
