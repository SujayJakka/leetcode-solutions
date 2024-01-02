class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        res = 0

        set_of_bs = set()
        row_dict, col_dict = {}, {}
        
        m, n = len(picture), len(picture[0])

        for i in range(m):
            row_dict[i] = 0

        for i in range(n):
            col_dict[i] = 0
        

        # populate dictionary

        for i in range(m):
            for j in range(n):
                if picture[i][j] == "B":
                    set_of_bs.add((i, j))
                    row_dict[i] += 1
                    col_dict[j] += 1
        

        for b in set_of_bs:
            i, j = b
            if row_dict[i] == 1 and col_dict[j] == 1:
                res += 1
        
        return res
