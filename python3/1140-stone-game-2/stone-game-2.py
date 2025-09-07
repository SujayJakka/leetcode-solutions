class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        dp = {}
        suffix_sum = [0] * len(piles)
        curr_suffix_sum = 0
        for i in range(len(piles) - 1, -1, -1):
            curr_suffix_sum += piles[i]
            suffix_sum[i] = curr_suffix_sum

        def dfs(curr_index, M):
            if curr_index >= len(piles):
                return 0
            
            if (curr_index, M) in dp:
                return dp[(curr_index, M)]
            
            res = 0
            for i in range(curr_index, curr_index + (2 * M)):
                res = max(res, suffix_sum[curr_index] - dfs(i + 1, max(M, i - curr_index + 1)))

            dp[(curr_index, M)] = res
            return res
        
        return dfs(0, 1)

        
