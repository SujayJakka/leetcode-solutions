class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        dp = []
        dp.append(nums[0])
        res = 1

        for i in range(1, len(nums)):
            if nums[i] > dp[-1]:
                dp.append(nums[i])
                res += 1
                continue

            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]

        return res


        