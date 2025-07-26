class Solution:
    def maxDifference(self, s: str) -> int:

        odd_count = 0
        even_count = float("inf")
        counter = Counter(s)

        for c in counter:
            if counter[c] % 2 == 0:
                even_count = min(even_count, counter[c])
            else:
                odd_count = max(odd_count, counter[c])
        
        return odd_count - even_count
        