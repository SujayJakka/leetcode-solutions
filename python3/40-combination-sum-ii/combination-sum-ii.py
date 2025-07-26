class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates = sorted(candidates)
        res = []
        curr = []


        def dfs(pos, target):
            if target == 0:
                res.append(curr.copy())
            if pos == len(candidates) or target <= 0:
                return
            
            prev = -1
            
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                
                curr.append(candidates[i])
                dfs(i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
        
        dfs(0, target)
        return res
        


        