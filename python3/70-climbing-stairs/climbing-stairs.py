class Solution:
    def climbStairs(self, n: int) -> int:
        memoization_map = {n:1}

        def dfs(current_step):
            if current_step in memoization_map:
                return memoization_map[current_step]
            elif current_step > n:
                return 0
            
            memoization_map[current_step] = dfs(current_step + 1) + dfs(current_step + 2)
            return memoization_map[current_step]
        
        return dfs(0)


            
            

            