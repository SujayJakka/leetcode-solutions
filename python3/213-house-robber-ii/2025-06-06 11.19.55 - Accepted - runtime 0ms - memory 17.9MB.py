class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(index, flag):
            if index >= len(nums) or (flag and index == len(nums) - 1):
                return 0
            elif memo[index][flag] != -1:
                return memo[index][flag]
            
            memo[index][flag] = max(dfs(index+1, flag), dfs(index+2, flag) + nums[index])

            return memo[index][flag]
        
        return max(dfs(0, True), dfs(1, False))