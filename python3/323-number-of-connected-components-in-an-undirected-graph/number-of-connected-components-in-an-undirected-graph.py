class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency_list = defaultdict(list)
        components = 0

        for a, b in edges:
            adjacency_list[a].append(b)
            adjacency_list[b].append(a)
        
        visited = set()
        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for new_node in adjacency_list[node]:
                dfs(new_node)
        

        for node in adjacency_list:
            if node not in visited:
                dfs(node)
                components += 1

        return n - len(visited) + components