class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:

        prefix = []
        curr = 0
        for num in nums:
            curr += num
            prefix.append(curr)
        res = []
        for i in range(len(nums)):
            curr = ((i - 0 + 1) * nums[i]) - (prefix[i])
            curr += ((prefix[-1] - prefix[i])) - (nums[i] * (len(nums) - i - 1))
            res.append(curr)
        return res
        