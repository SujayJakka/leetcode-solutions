class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        res = []

        def two_sum(i, target):
            l, r = i + 1, len(nums) - 1
            temp = []
            while l < r:
                if nums[l] + nums[r] == target:
                    temp.append([nums[i], nums[l], nums[r]])

                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
            return temp
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            temp = two_sum(i, 0 - nums[i])
            res += temp
        
        return res