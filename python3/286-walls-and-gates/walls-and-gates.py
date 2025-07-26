from collections import deque

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        visited = set()
        queue = deque()
        n, m = len(rooms), len(rooms[0])

        for i in range(n):
            for j in range(m):
                if rooms[i][j] != 0:
                    continue
                
                visited.add((i, j))
                queue.append((i, j))

        level = 0
        while queue:
            for _ in range(len(queue)):
                new_i, new_j = queue.popleft()

                if rooms[new_i][new_j] == -1:
                    continue
                else:
                    rooms[new_i][new_j] = level

                if new_i + 1 < n and (new_i + 1, new_j) not in visited:
                    visited.add((new_i + 1, new_j))
                    queue.append((new_i + 1, new_j))
                if new_i - 1 >= 0 and (new_i - 1, new_j) not in visited:
                    visited.add((new_i - 1, new_j))
                    queue.append((new_i - 1, new_j))
                if new_j + 1 < m and (new_i, new_j + 1) not in visited:
                    visited.add((new_i, new_j + 1))
                    queue.append((new_i, new_j + 1))
                if new_j - 1 >= 0 and (new_i, new_j - 1) not in visited:
                    visited.add((new_i, new_j - 1))
                    queue.append((new_i, new_j - 1))
            
            level += 1
                        