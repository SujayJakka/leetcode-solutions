class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        counter = Counter(nums)
        res = []

        def dfs(arr):

            if len(arr) == len(nums):
                res.append(arr.copy())
            
            for n in counter:
                if counter[n] != 0:
                    counter[n] -= 1
                    arr.append(n)
                    dfs(arr)
                    arr.pop()
                    counter[n] += 1

        dfs([])
        return res
                

        
        
