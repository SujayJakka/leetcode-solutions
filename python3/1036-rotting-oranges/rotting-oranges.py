from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rotten_oranges = 0
        empty_cells = 0
        time = 0
        map_thing = {}
        my_queue = deque()
        visited = set()

        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 2:
                    visited.add((i, j))
                    my_queue.append((i, j))
                    rotten_oranges += 1

                if grid[i][j] == 0:
                    empty_cells += 1

        
        max_rotten = (len(grid) * len(grid[0])) - empty_cells

        if max_rotten == rotten_oranges:
            return 0

        #BFS


        while(my_queue):

            for _ in range(len(my_queue)):

                (i, j) = my_queue.popleft()

                if i - 1 >= 0:
                    if grid[i-1][j] == 1 and (i-1, j) not in visited:
                        visited.add((i-1, j))
                        my_queue.append((i-1, j))
                        rotten_oranges += 1

                if i + 1 < len(grid):
                    if grid[i+1][j] == 1 and (i+1, j) not in visited:
                        visited.add((i+1, j))
                        my_queue.append((i+1, j))
                        rotten_oranges += 1
                
                if j - 1 >= 0:
                    if grid[i][j-1] == 1 and (i, j-1) not in visited:
                        visited.add((i, j-1))
                        my_queue.append((i, j-1))
                        rotten_oranges += 1

                if j + 1 < len(grid[0]):
                    if grid[i][j+1] == 1 and (i, j+1) not in visited:
                        visited.add((i, j+1))
                        my_queue.append((i, j+1))
                        rotten_oranges += 1
            
            time += 1
        
        time -= 1

        return time if max_rotten == rotten_oranges else -1
        


        