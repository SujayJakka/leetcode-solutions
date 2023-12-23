class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums[0])
        nums_set = set(nums)
        
        answer = [None]
        
        def decision_function(curr, i):
            
            if i > n:
                
                if curr not in nums_set:
                    answer[0] = curr
        
                return
            
            decision_function(curr + "0", i+1)
            
            if answer[0] is not None:
                return
            
            decision_function(curr + "1", i+1)
            
        
        decision_function("", 1)
        
        return answer[0]
            
