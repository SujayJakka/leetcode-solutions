class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def DFS(i, curr, total):

            if(total == target):
                res.append(curr.copy())
                return
            
            if(total > target) or i >= len(candidates):
                return
            
            curr.append(candidates[i])
            DFS(i, curr, total + candidates[i])
            curr.pop()
            DFS(i+1, curr, total)

        DFS(0, [], 0)    
        
        return res
