class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        adjacency_map = {c:set() for w in words for c in w}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjacency_map[w1[j]].add(w2[j])
                    break

        visited = {}
        res = []

        def topological_sort(node, res):
            if node in visited:
                return visited[node]
            
            visited[node] = True

            for new_node in adjacency_map[node]:
                if topological_sort(new_node, res):
                    return True

            visited[node] = False
            res.append(node)
            return False
        

        for node in adjacency_map:
            if topological_sort(node, res):
                return ""
        
        return "".join(res[::-1])
        

        


        