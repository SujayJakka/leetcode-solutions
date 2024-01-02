class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        parentArr = [0] * n
        sizeArr = [1] * n

        res = n

        for i in range(n):
            parentArr[i] = i
        
        def find(i):
            if i == parentArr[i]:
                return i
            else:
                return find(parentArr[i])

        
        for edge in edges:
            p1 = find(edge[0])
            p2 = find(edge[1])

            if p1 != p2:

                if sizeArr[p1] >= sizeArr[p2]:
                    sizeArr[p1] += sizeArr[p2]
                    parentArr[p2] = p1
                else:
                    sizeArr[p2] += sizeArr[p1]
                    parentArr[p1] = p2
                res -= 1
        
        return res
  
