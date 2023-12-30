class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        map_thing = {}
        
        for i in range(len(numbers)):
            if (target - numbers[i]) in map_thing:
                return [map_thing[target - numbers[i]], i + 1]
            else:
                map_thing[numbers[i]] = i + 1
