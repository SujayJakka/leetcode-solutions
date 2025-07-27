class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        nums = sorted(nums)[::-1]

        total_sum = sum(nums)

        if total_sum % k != 0:
            return False
        
        target = total_sum / k
        used = [False] * len(nums)

        def dfs(curr_index, k, curr_subset_sum):
            if k == 0:
                return True
            
            if curr_subset_sum == target:
                return dfs(0, k - 1, 0)
            
            for i in range(curr_index, len(nums)):
                if not used[i] and curr_subset_sum + nums[i] <= target:
                    used[i] = True
                    if dfs(i + 1, k, curr_subset_sum + nums[i]):
                        return True
                    used[i] = False

                    if curr_subset_sum == 0:
                        return False
            
            return False
        
        return dfs(0, k, 0)
