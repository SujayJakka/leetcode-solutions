class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        length = sum(matchsticks) // 4
        if sum(matchsticks) % 4 != 0:
            return False
        
        arr = [0] * 4

        matchsticks.sort(reverse=True)
        
        def backtrack(i):
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if matchsticks[i] + arr[j] <= length:
                    arr[j] += matchsticks[i]
                    if backtrack(i + 1):
                        return True
                    arr[j] -= matchsticks[i]
            
            return False
        
        return backtrack(0)