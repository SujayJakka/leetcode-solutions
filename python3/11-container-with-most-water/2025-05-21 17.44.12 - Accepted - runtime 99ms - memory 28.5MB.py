class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            temp_height = min(height[l], height[r])

            res = max(res, temp_height * (r - l))

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1

        return res
