class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return nums[0]
        rob1, rob2 = 0,0
        route1, route2 = 0,0 
        for i in range(1, len(nums)):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp
        route1 = rob2
        rob1, rob2 = 0,0

        for i in range(0, len(nums) - 1):
            temp = max(rob2, rob1 + nums[i])
            rob1 = rob2
            rob2 = temp
        route2 = rob2

        return route1 if route1 > route2 else route2


