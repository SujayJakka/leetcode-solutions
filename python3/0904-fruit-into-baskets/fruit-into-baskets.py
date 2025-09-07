class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        res = 0
        h_map = defaultdict(int)

        l = 0

        for r in range(len(fruits)):
            # Add fruit to h_map
            h_map[fruits[r]] += 1
            

            # Remove if there are more than two types of fruits
            while len(h_map) > 2:
                h_map[fruits[l]] -= 1
                if h_map[fruits[l]] == 0:
                    h_map.pop(fruits[l])
                l += 1


            # Calculate number of fruits in basket and update res
            res = max(res, r - l + 1)

        return res
        
