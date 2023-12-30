class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lp = [1] * len(nums)
        rp = [1] * len(nums)
        lp[0] = nums[0]
        rp[-1] = nums[-1]

        res = []

        for i in range(1, len(nums)):
            lp[i] = nums[i] * lp[i-1]
        for i in range(len(nums)-2, -1, -1):
            rp[i] = nums[i] * rp[i+1]
        

        for i in range(len(nums)):

            if i == 0:
                res.append(rp[1])
            elif i == len(nums) - 1:
                res.append(lp[-2])
            else:
                res.append(lp[i-1] * rp[i+1])

        return res
        
