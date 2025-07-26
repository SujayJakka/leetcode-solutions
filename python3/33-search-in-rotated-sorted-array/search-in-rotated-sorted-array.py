class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1


        while l <= r:

            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[r]:
                if nums[mid] > target:
                    r -= 1
                else:
                    l += 1
            else:
                if target > nums[r]:
                    r -= 1
                else:
                    l += 1
        
        return -1

        