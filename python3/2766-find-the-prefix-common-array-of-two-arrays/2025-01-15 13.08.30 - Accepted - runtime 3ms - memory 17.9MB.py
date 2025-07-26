class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        my_set = set()
        res = []
        curr = 0

        for i in range(len(B)):
            if A[i] == B[i]:
                curr += 1
                res.append(curr)
                my_set.add(A[i])
                continue

            if A[i] in my_set:
                curr += 1
            if B[i] in my_set:
                curr += 1

            res.append(curr)
            my_set.add(A[i])
            my_set.add(B[i])
        
        return res



        