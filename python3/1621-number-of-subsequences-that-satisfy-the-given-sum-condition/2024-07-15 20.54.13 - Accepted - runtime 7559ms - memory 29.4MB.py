class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = 0
        r = len(nums) - 1

        for i in range(len(nums)):
            while nums[i] + nums[r] > target and i <= r:
                r -= 1
            
            if i <= r:
                res += (2**(r - i))
                res %= (10**9 + 7)
        
        return res




        