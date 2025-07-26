class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        count = Counter(nums)
        nums = sorted(list(set(nums)))

        earn_1, earn_2 = 0, 0

        for i in range(len(nums)):
            curr_earn = nums[i] * count[nums[i]]

            if i > 0 and nums[i] == nums[i - 1] + 1:
                temp = earn_2
                earn_2 = max(earn_1 + curr_earn, earn_2)
                earn_1 = temp
            else:
                temp = earn_2
                earn_2 = earn_2 + curr_earn
                earn_1 = temp
        
        return earn_2

        