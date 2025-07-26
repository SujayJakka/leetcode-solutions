class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1
        
        amountOfGas = 0
        start = 0
                
        for i in range(len(gas)):
            
            amountOfGas += (gas[i] - cost[i])

            if amountOfGas < 0:
                start = i + 1
                amountOfGas = 0

        return start
            

