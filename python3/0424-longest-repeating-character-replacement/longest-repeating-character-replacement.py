class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h_map = defaultdict(int)
        res = 0
        l, r = 0, 0

        max_freq = 0


        while r < len(s):

            h_map[s[r]] += 1

            max_freq = max(max_freq, h_map[s[r]])

            if max_freq + k < r - l + 1:
                h_map[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1

        return res






