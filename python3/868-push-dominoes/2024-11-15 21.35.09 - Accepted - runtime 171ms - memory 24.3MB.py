from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        dominoes = list(dominoes)
        queue = deque()

        for i, d in enumerate(dominoes):
            if d != ".": queue.append((i, d))
    

        while queue:
            i, d = queue.popleft()
            if i - 1 > -1 and dominoes[i - 1] == "." and d == "L":
                dominoes[i - 1] = "L"
                queue.append((i - 1, "L"))
            
            if i + 1 < len(dominoes) and dominoes[i + 1] == "." and d == "R":
                if i + 2 < len(dominoes) and dominoes[i + 2] == "L":
                    queue.popleft()
                else:
                    dominoes[i + 1] = "R"
                    queue.append((i + 1, "R"))
        
        return "".join(dominoes)
                



            
                
                
        