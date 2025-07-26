import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges_map = {}
        distance_dict = {}
        min_heap = []

        for i in range(1, n+1):
            edges_map[i] = []
        
        for edge in times:
            edges_map[edge[0]].append((edge[1], edge[2]))

        visited = set()
        heapq.heappush(min_heap, [0, k])
        distance_dict[k] = 0
        for i in range(1, n+1):
            if i != k:
                heapq.heappush(min_heap, [float("inf"), i])
                distance_dict[i] = float("inf")
        
        def relax(s_node, e_node, weight):
            if distance_dict[s_node] + weight < distance_dict[e_node]:
                distance_dict[e_node] = distance_dict[s_node] + weight
                for i in range(len(min_heap)):
                    distance, node = min_heap[i]
                    if node == e_node:
                        min_heap[i][0] = distance_dict[e_node]
                heapify(min_heap)

        while len(min_heap) != 0:
            distance, node = heapq.heappop(min_heap)
            if distance == float("inf"):
                return -1
            visited.add(node)

            for edge in edges_map[node]:
                e_node, weight = edge
                if e_node not in visited:
                    relax(node, e_node, weight)
        
        return distance
        







