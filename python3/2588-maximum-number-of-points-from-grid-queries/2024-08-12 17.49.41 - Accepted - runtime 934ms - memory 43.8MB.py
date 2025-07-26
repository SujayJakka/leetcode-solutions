import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        ROWS, COLS = len(grid), len(grid[0])
        query_to_res = {}
        new_queries = sorted(queries)
        res = []
        points = 0
        min_heap = []
        visit = set()

        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        visit.add((0, 0))

        for query in new_queries:
            while min_heap and query > min_heap[0][0]:
                _, i, j = heapq.heappop(min_heap)
                points += 1

                directions = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

                for new_i, new_j in directions:
                    if 0 <= new_i < ROWS and 0 <= new_j < COLS and (new_i, new_j) not in visit:
                        visit.add((new_i, new_j))
                        heapq.heappush(min_heap, (grid[new_i][new_j], new_i, new_j))

            query_to_res[query] = points
        
        for this_query in queries:
            res.append(query_to_res[this_query])
        
        return res


                    



            
            



        

        