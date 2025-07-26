class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        curr = []

        def dfs(pos):
            if pos == len(nums):
                res.append(curr[:])
                return
            for i in range(len(nums)):
                if nums[i] == -11:
                    continue

                temp = nums[i]
                curr.append(temp)
                nums[i] = -11
                dfs(pos + 1)
                curr.pop()
                nums[i] = temp
            
        dfs(0)
        return res
        