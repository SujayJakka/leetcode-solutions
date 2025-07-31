class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        result = 0
        hm = Counter()
        for num in deliciousness:
            for i in range(22): 
                thing = 2**i-num
                tempVar = hm[thing]
                result += tempVar
            hm[num] += 1
        return result % ((10 ** 9) + 7)
        