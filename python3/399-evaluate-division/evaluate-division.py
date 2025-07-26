class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adj_list = defaultdict(list)

        def dfs(node, target, visited):
            
            if node not in adj_list or target not in adj_list:
                return -1

            if node == target:
                return 1
            
            visited.add(node)
            
            for next_node, weight in adj_list[node]:
                if next_node not in visited:
                    val = dfs(next_node, target, visited)
                
                    if val != -1:
                        return weight * val

            return -1


        for i in range(len(equations)):
            a, b = equations[i]
            val = values[i]

            adj_list[a].append((b, val))
            adj_list[b].append((a, 1/val))
        

        return [dfs(a, b, set()) for a, b in queries]
        