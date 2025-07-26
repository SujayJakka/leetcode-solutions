class Solution:
    def rob(self, nums: List[int]) -> int:

        # Top Down
        # memoization_map = {}

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     elif i in memoization_map:
        #         return memoization_map[i]
            
        #     # Two options either rob the house or skip
        #     memoization_map[i] = max(nums[i] + dfs(i + 2), dfs(i + 1))
        #     return memoization_map[i]
        
        # return dfs(0)

        # Bottom Up 
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        
        arr = [0] * len(nums)
        arr[0] = nums[0]
        arr[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            arr[i] = max(arr[i - 1], nums[i] + arr[i - 2])
        
        return arr[-1]

        