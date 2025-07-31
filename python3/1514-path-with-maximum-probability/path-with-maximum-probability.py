import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        edges_dictionary = defaultdict(list)
        
        for i in range(len(edges)):
            a, b = edges[i]
            prob = succProb[i]
            edges_dictionary[a].append((b, prob))
            edges_dictionary[b].append((a, prob))
    
        
        max_heap = []
        heapq.heappush(max_heap, (-1, start_node))
        visit = set()

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            if node == end_node:
                return prob * -1
            
            if node in visit:
                continue
            
            visit.add(node)
            
            for b, new_prob in edges_dictionary[node]:
                if b not in visit:
                    heapq.heappush(max_heap, (new_prob * prob, b))
            
        return 0
        


        
