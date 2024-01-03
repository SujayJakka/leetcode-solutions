class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjList = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            numIterations = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:numIterations] == w2[:numIterations]:
                return ""
            for j in range(numIterations):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        visit = {}
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True

            for nei in adjList[c]:
                if dfs(nei):
                    return True
            
            visit[c] = False
            res.append(c)
        

        for c in adjList:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)
