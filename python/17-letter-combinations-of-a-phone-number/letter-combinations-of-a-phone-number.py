class Solution(object):
    def letterCombinations(self, digits):
        thing = []
        if(len(digits) == 0):
            return thing
        lettermap = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        for s in digits:
            options = lettermap[s]
            thing.append(options)
        result = list(itertools.product(*thing))
        for i in range(0, len(result)):
            thing = result[i]
            newthing = "".join(thing)
            result[i] = newthing
        return result
            
            
        
        
        