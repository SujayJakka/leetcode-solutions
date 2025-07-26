class DetectSquares:

    def __init__(self):
        self.h_map = defaultdict(int)
        self.points = []
        

    def add(self, point: List[int]) -> None:
        self.h_map[(point[0], point[1])] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:

        res = 0

        for x, y in self.points:
            if (abs(x - point[0]) == abs(y - point[1])) and [x, y] != point:
                res += (self.h_map[(x, point[1])] * self.h_map[(point[0], y)])
        return res

        

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)