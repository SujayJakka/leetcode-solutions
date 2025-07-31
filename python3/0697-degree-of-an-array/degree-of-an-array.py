class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, defaultdict(int)

        for i, x in enumerate(nums):
            if x not in left:
                left[x] = i 
            right[x] = i
            count[x] += 1
        
        max_value = max(count.values())
        res = float("inf")

        for key in count:
            if count[key] == max_value:
                res = min(res, right[key] - left[key] + 1)
            
        return res
