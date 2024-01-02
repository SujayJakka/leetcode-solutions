class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapThing = {}

        for i in range(len(nums)):
            if nums[i] in mapThing:
                mapThing[nums[i]] += 1
            else:
                mapThing[nums[i]] = 1
        
        sorted_keys = sorted(mapThing.keys(), key=lambda k: mapThing[k])

        return sorted_keys[-k:]
