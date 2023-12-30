class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setThing = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in setThing:
                curr = 1
                while(n + curr in setThing):
                    curr += 1
                if curr > res:
                    res = curr
        return res
