class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        x_y, y_x = 0, 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == "x":
                    x_y += 1
                else:
                    y_x += 1

        if (x_y + y_x) % 2 == 1:
            return -1
        
        swaps = 0
        swaps += (x_y // 2)
        swaps += (y_x // 2)

        if x_y % 2 == 1:
            swaps += 2
        
        return swaps
        
        