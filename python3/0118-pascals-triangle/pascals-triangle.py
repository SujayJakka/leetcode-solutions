class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        for i in range(numRows):
            new_arr = [1] * (i + 1)

            for j in range(1, i):
                new_arr[j] = res[-1][j] + res[-1][j-1]

            res.append(new_arr)
        return res
