class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:

        target = 0

        for num in nums:
            target |= num
        
        memo = {}

        def dfs(index, curr):
            if index == len(nums):
                if curr == target:
                    return 1
                return 0
            
            if (index, curr) in memo:
                return memo[(index, curr)]
            
            # Take
            take = dfs(index + 1, curr | nums[index])

            # Skip
            skip = dfs(index + 1, curr)

            memo[(index, curr)] = take + skip
            return memo[(index, curr)]
        
        return dfs(0, 0)
