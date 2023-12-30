class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        res = max(nums)
        currMax, currMin = 1,1

        for n in nums:
            if n == 0:
                currMax = 1
                currMin = 1
                continue
            
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp, currMin * n, n)

            res = max(currMax, res)
        
        return res
