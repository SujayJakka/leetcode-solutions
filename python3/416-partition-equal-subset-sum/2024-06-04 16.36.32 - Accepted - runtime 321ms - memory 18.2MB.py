class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) / 2

        DP = set()
        DP.add(0)

        for i in range(len(nums)):

            next_DP = set()

            for element in DP:
                if element + nums[i] == target:
                    return True
                
                next_DP.add(element)
                next_DP.add(element + nums[i])
            
            DP = next_DP
            
        return False
            

        


        