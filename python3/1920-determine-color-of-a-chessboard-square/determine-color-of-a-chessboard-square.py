class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        h_map = {"a" : 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
        if (h_map[coordinates[0]] + int(coordinates[1])) % 2:
            return True
        else:
            return False