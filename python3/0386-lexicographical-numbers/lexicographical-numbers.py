class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        curr = 1

        for _ in range(n):
            res.append(curr)

            if curr * 10 <= n:
                curr = curr * 10
                continue
            
            while curr % 10 == 9 or curr == n:
                curr //= 10
            curr += 1

        return res