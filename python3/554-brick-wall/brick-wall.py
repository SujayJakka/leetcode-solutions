class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h_map = defaultdict(int)

        for row in wall:
            curr_sum = 0
            for col in row:
                curr_sum += col
                h_map[curr_sum] += 1
        
        max_value = 0
        width = sum(wall[0])
        for key in h_map:

            if key == width:
                continue

            if max_value < h_map[key]:
                max_value = h_map[key]

        return len(wall) - max_value




        