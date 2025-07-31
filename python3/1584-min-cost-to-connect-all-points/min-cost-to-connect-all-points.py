class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        edges_list = []
        cost = 0

        for i in range(len(points) - 1):
            for j in range(i+1, len(points)):
                distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges_list.append([distance, i, j])
        
        edges_list = sorted(edges_list, key=lambda x: x[0])
        
        parent_arr = [[0,1] for _ in range(len(points))]

        for i in range(len(parent_arr)):
            parent_arr[i][0] = i
    
        
        def find_parent(child):
            if parent_arr[child][0] == child:
                return child
            
            return find_parent(parent_arr[child][0])
        
        
        for edge in edges_list:
            distance, u, v = edge

            parent_u = find_parent(u)
            parent_v = find_parent(v)
            
            if parent_u == parent_v:
                continue
            
            cost += distance

            size_parent_u = parent_arr[parent_u][1]
            size_parent_v = parent_arr[parent_v][1]

            if size_parent_u < size_parent_v:
                parent_arr[parent_u][0] = parent_v
                parent_arr[parent_v][1] += size_parent_u
            else:
                parent_arr[parent_v][0] = parent_u
                parent_arr[parent_u][1] += size_parent_v

        return cost



        