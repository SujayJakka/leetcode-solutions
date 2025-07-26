class Solution:
    def digitCount(self, num: str) -> bool:
        h_map = defaultdict(int)

        for c in num:
            h_map[int(c)] += 1
        
        for i, c in enumerate(num):
            if h_map[i] != int(c):
                return False
        return True
        