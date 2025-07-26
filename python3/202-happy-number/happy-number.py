class Solution:
    def isHappy(self, n: int) -> bool:
        arrThing = set()
        arrThing.add(n)

        while n != 1:
            numThing = []

            while n != 0:
                numThing.append(n % 10)
                n = n // 10
            
            n = 0
            
            for num in numThing:
                n += num ** 2
            
            if n in arrThing:
                return False
            
            arrThing.add(n)

        return True