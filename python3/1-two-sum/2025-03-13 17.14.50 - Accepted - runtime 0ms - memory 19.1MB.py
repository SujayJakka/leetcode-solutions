class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, num in enumerate(nums):
            if target - num in h_map:
                return [h_map[target - num], i]

            h_map[num] = i