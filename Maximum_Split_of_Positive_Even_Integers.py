class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if(finalSum % 2 != 0):
            return []
        numOfTwos = finalSum // 2
        remSum = finalSum
        result = []
        for i in range(1, numOfTwos + 1):
            if(remSum == 0):
                break
            if((2*i) <= remSum):
                result.append((2*i))
                remSum -= (2*i)
            else:
                result[-1] += remSum
                remSum -= remSum
        return result
                
            
            
        
