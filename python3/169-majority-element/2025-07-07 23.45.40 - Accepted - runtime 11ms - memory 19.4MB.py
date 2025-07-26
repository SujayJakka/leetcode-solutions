class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h_map = {}
        max_freq = 0
        res = None

        for num in nums:
            if num not in h_map:
                h_map[num] = 1
            else:
                h_map[num] += 1
        
            if h_map[num] > max_freq:
                max_freq = h_map[num]
                res = num
        
        return res
            
