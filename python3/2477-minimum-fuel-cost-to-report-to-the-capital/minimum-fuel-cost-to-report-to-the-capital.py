class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        adj_list = defaultdict(list)
        for beg, end in roads:
            adj_list[beg].append(end)
            adj_list[end].append(beg)
        
        res = 0
        
        def dfs(node, parent):

            nonlocal res
            passengers = 0

            for child in adj_list[node]:
                if child != parent:
                    p = dfs(child, node)
                    res += ceil(p / seats)
                    passengers += p
            
            return passengers + 1
        
        dfs(0, -1)
        return res
        