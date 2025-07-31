import heapq
from collections import deque
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counter = Counter(tasks)
        max_heap = [-count for count in counter.values()]
        heapq.heapify(max_heap)
        
        time = 0
        queue = deque()


        def add_to_max_heap(time):
            if len(queue) > 0:
                if time == queue[0][1]:
                    new_task = queue.popleft()
                    heapq.heappush(max_heap, new_task[0])


        while max_heap or queue:

            if len(max_heap) == 0:
                time += 1
                add_to_max_heap(time)
                continue

            task = heapq.heappop(max_heap)
            task += 1

            time += 1

            if task != 0:
                queue.append((task, time + n))

            add_to_max_heap(time)

        return time
            
                




        
        