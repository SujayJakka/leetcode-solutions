class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currentSum = 0

        for i in range(len(nums)):

            if (currentSum + nums[i]) < nums[i]:
                currentSum = nums[i]
                if maxSum < currentSum:
                    maxSum = currentSum
            
            else:
                currentSum += nums[i]
                if maxSum < currentSum:
                    maxSum = currentSum
        return maxSum

