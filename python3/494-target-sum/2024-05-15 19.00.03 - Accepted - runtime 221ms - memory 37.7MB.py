class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        h_map = {}
        def recursive_method(count, curr):
            if count == len(nums):
                if curr == target:
                    return 1
                else:
                    return 0
            
            if (count, curr) in h_map:
                return h_map[(count, curr)]
            
            h_map[(count, curr)] = recursive_method(count + 1, curr - nums[count]) + recursive_method(count + 1, curr + nums[count])
            return h_map[(count, curr)]
        
        return recursive_method(0, 0)

       
        