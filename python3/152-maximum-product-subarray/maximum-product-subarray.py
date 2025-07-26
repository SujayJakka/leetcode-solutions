class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = nums[0]
        running_product_max = 1
        running_product_min = 1

        for i in range(len(nums)):
            old_running_max = running_product_max
            running_product_max = max(nums[i], nums[i] * running_product_max, nums[i] * running_product_min)
            running_product_min = min(nums[i], nums[i] * old_running_max, nums[i] * running_product_min)
            res = max(running_product_max, res)
        
        return res