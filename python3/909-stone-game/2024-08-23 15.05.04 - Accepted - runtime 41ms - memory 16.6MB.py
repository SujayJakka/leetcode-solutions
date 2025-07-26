class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # dp = {}
        # target = ceil(sum(piles) / 2)

        # def dfs(i, j):
        #     if i > j:
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     even = True if (j - i) % 2 else False
        #     left = piles[i] if even else 0
        #     right = piles[j] if even else 0
            
        #     dp[(i, j)] = max(dfs(i + 1, j) + left, dfs(i, j - 1) + right)
        #     return dp[(i, j)]
        
        # if dfs(0, len(piles) - 1) >= target:
        #     return True
        # else:
        #     return False

        return True