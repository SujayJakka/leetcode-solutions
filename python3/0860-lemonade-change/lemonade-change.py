class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        h_map = defaultdict(int)


        for bill in bills:
            
            h_map[bill] += 1
            change = bill - 5

            if change == 15:
                if h_map[10] >= 1 and h_map[5] >= 1:
                    h_map[10] -= 1
                    h_map[5] -= 1
                elif h_map[5] >= 3:
                    h_map[5] -= 3
                else:
                    return False
            
            elif change == 5:
                if h_map[5] != 0:
                    h_map[5] -= 1
                else:
                    return False

        return True
        