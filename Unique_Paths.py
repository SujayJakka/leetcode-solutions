class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        hmap = {}
        if m > 1 and n > 1:
            return 2 + self.uniquePaths2(m-1, n, hmap) + self.uniquePaths2(m, n-1, hmap)
        else:
            return 1

    def uniquePaths2(self, m: int, n: int, hmap) -> int:
        result = 0

        if tuple([m,n]) in hmap.keys():
            return hmap[m,n]

        if m > 1 and n > 1:
            result = 1 + self.uniquePaths2(m-1, n, hmap) + self.uniquePaths2(m, n-1, hmap)
            hmap[tuple([m,n])] = result
            return result
        else:
            hmap[tuple([m,n])] = 0
            return 0  
