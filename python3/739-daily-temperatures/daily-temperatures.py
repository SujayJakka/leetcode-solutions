class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stackThing = []
        res = [0] * len(temperatures)


        for curr_day, curr_temp in enumerate(temperatures):
            while stackThing:
                if curr_temp > temperatures[stackThing[-1]]:
                    days = curr_day - stackThing[-1]
                    res[stackThing[-1]] = days
                    stackThing.pop()
                else:
                    break
            stackThing.append(curr_day)
        
        return res