class Solution:
    def validPartition(self, nums: List[int]) -> bool:


        cache = set()

        def dfs(i):

            if i == len(nums):
                return True
            
            if i in cache:
                return False
            
            if i < len(nums) - 1 and nums[i] == nums[i + 1]:
                if dfs(i + 2):
                    return True
            if i < len(nums) - 2 and nums[i] == nums[i + 1] == nums[i + 2]:
                if dfs(i + 3):
                    return True
            if i < len(nums) - 2 and nums[i] + 2 == nums[i + 1] + 1 == nums[i + 2]:
                if dfs(i + 3):
                    return True
            
            cache.add(i)
            return False
        
        return dfs(0)