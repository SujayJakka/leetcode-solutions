class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if ((m - 1 < 0 or nums[m - 1] != nums[m]) and (m + 1 == len(nums) or nums[m] != nums[m + 1])):
                return nums[m]
            
            left_size = m - 1 if nums[m - 1] == nums[m] else m
            if left_size % 2:
                r = m - 1
            else:
                l = m + 1