class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        for i in range(0, len(nums)):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp
        return rob2
