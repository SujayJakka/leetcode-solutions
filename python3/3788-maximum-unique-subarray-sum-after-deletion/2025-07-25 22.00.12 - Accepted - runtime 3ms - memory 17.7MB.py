class Solution:
    def maxSum(self, nums: List[int]) -> int:

        res = 0
        my_set = set()

        for num in nums:
            if num > 0 and num not in my_set:
                res += num
                my_set.add(num)
        
        if res == 0:
            return max(nums)
        else:
            return res
        