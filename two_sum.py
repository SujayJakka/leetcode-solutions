class Solution(object):
    def twoSum(self, nums, target):
        h_map = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in h_map:
                return [h_map[diff], i]
            else:
                h_map[nums[i]] = i
