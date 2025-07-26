class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []

        def dfs(index, curr, remaining):
            
            if remaining == 0:
                res.append(curr.copy())
                return
            elif remaining < 0 or index == len(candidates):
                return
            

            # Option 1: Choose number at index
            curr.append(candidates[index])
            dfs(index, curr, remaining - candidates[index])
            curr.pop()

            # Option 2: Skip over number
            dfs(index + 1, curr, remaining)

        dfs(0, [], target)
        return res


        