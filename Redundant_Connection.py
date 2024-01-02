class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0

        for num1, num2 in edges:
            if num1 > n:
                n = num1
            if num2 > n:
                n = num2
        
        disjointArr = [0] * n
        sizeArr = [1] * n

        for i in range(len(disjointArr)):
            disjointArr[i] = i
        

        def find(i):
            if disjointArr[i] == i:
                return i
            else:
                return find(disjointArr[i])
        

        for num1, num2 in edges:
            p1 = find(num1 - 1)
            p2 = find(num2 - 1)

            if p1 == p2:
                return [num1, num2]
            
            if sizeArr[p1] >= sizeArr[p2]:
                sizeArr[p1] += 1
                disjointArr[p2] = p1
            else:
                sizeArr[p2] += 1
                disjointArr[p1] = p2

