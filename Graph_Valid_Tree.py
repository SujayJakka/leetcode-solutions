class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        res = n
        
        parentArr = [0] * n
        sizeArr = [1] * n

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

            if p1 == p2:
                return False
            else:
                if p1 > p2:
                    parentArr[p2] = p1
                    sizeArr[p1] += sizeArr[p2]
                else:
                    parentArr[p1] = p2
                    sizeArr[p2] += sizeArr[p1]
                res -= 1    
        
        if res == 1:
            return True
        else:
            return False


        
