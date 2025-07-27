class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:

        for i in range(len(conflictingPairs)):
            a, b = conflictingPairs[i]
            if a > b:
                conflictingPairs[i] = [b, a]

        sorted_pairs = sorted(conflictingPairs, key=lambda x: x[1])

        total_sub_arrays = (n * (n + 1)) / 2
        max_1, max_2 = 0, 0
        max_profit, curr_profit = 0, 0
        blocked = 0

        for i in range(len(sorted_pairs)):
            start, end = sorted_pairs[i]
            
            if start > max_1:
                max_2 = max_1
                max_1 = start
                curr_profit = 0
            elif start > max_2:
                max_2 = start
            
            next_end = n + 1
            if i + 1 < len(sorted_pairs):
                next_end = sorted_pairs[i+1][1]

            blocked += (max_1 * (next_end - end))
            curr_profit += ((max_1 - max_2) * (next_end - end))

            max_profit = max(curr_profit, max_profit)

        return int(total_sub_arrays - blocked + max_profit)
