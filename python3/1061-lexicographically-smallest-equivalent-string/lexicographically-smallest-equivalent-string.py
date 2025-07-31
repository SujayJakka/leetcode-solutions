class DisjointSet:
    def __init__(self):
        self.parent = {}
        for c in "abcdefghijklmnopqrstuvwxyz":
            self.parent[c] = c
    
    def find(self, c):
        if self.parent[c] == c:
            return c
        self.parent[c] = self.find(self.parent[c])
        return self.parent[c]
    
    def union(self, c_1, c_2):
        parent_c_1 = self.find(c_1)
        parent_c_2 = self.find(c_2)

        if parent_c_1 == parent_c_2:
            return
        
        if parent_c_1 < parent_c_2:
            self.parent[parent_c_2] = parent_c_1
        else:
            self.parent[parent_c_1] = parent_c_2


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        res = []

        disjoint_set = DisjointSet()

        for i in range(len(s1)):
            c_1, c_2 = s1[i], s2[i]
            disjoint_set.union(c_1, c_2)
        
        for c in baseStr:
            res.append(disjoint_set.find(c))

        return "".join(res)