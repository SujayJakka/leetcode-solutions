class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        res = 0

        for num in nums:

            if num + 1 in nums:
                continue
            
            temp_res = 1

            while num - temp_res in nums:
                temp_res += 1
            
            res = max(temp_res, res)
        

        return res
            
