class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        h_map = defaultdict(int)
        h_map[0] = 1
        sum = 0

        for num in nums:
            sum += num
            if sum - k in h_map:
                res += h_map[sum - k]
            h_map[sum] += 1
        
        return res
