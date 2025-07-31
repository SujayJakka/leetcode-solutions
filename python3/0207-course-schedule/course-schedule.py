class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = defaultdict(list)

        for a, b in prerequisites:
            adjacency_list[b].append(a)
            if a not in adjacency_list:
                adjacency_list[a] = []
        
        visited = set()
        
        def dfs(prereq, path):
            if prereq in path:
                return False
            elif prereq in visited:
                return True
            
            visited.add(prereq)
            path.add(prereq)
            for course in adjacency_list[prereq]:
                if not dfs(course, path):
                    return False
            
            path.remove(prereq)
            return True
        
        for prereq in adjacency_list:
            if not dfs(prereq, set()):
                return False
        return True
        