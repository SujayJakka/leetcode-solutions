class Solution:
    def clearStars(self, s: str) -> str:
        
        min_heap = []

        for i, c in enumerate(s):
            if c != "*":
               heappush(min_heap, (c, -i))
            else:
                heappop(min_heap)
        
        res = [""] * len(s)

        for c, i in min_heap:
            res[-i] = c
        
        return "".join(res)









        
        