class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        l = 0
        r = len(height) - 1

        while(l < r):
            minThing = min(height[l], height[r])

            temp = minThing * (r - l)

            if(temp > res):
                res = temp

            if(height[l] < height[r]):
                l+=1
            
            else:
                r-=1
        
        return res
