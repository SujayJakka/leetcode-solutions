class Solution:
    def maxDistance(self, s: str, k: int) -> int:

        res = 0
        latitude = longitude = 0

        for i, c in enumerate(s):
            if c == "N":
                longitude += 1
            elif c == "S":
                longitude -= 1
            elif c == "W":
                latitude -= 1
            else:
                latitude += 1
            
            res = max(res, min(abs(longitude) + abs(latitude) + 2 * k, i + 1))

        return res
        