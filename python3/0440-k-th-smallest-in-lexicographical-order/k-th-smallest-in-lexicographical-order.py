class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        
        def find_steps(prefix_1, prefix_2):

            steps = 0
            while prefix_1 <= n:
                steps += min(n + 1, prefix_2) - prefix_1
                prefix_1 *= 10
                prefix_2 *= 10

            return steps
        
        curr = 1
        k -= 1

        while k > 0:
            steps = find_steps(curr, curr + 1)

            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1
        
        return curr