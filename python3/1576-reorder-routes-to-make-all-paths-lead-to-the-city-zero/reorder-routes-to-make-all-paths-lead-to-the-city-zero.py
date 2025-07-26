class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        edges_map = defaultdict(list)
        for a, b in connections:
            edges_map[a].append((b, 1))
            edges_map[b].append((a, 0))
        
        res = [0]

        def dfs(node):
            visited.add(node)
            for des, val in edges_map[node]:
                if des not in visited:
                    res[0] += val
                    dfs(des)

        dfs(0)
        return res[0]
        