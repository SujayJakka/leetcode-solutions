class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        counter = Counter(s)
        max_heap = [(-count, c) for c, count in counter.items()]
        heapify(max_heap)

        prev = None

        while max_heap or prev:
            if prev and not max_heap:
                return ""
            
            freq, c = heappop(max_heap)

            res.append(c)
            freq += 1

            if prev:
                heappush(max_heap, prev)
                prev = None
            
            if freq != 0:
                prev = (freq, c)

        return "".join(res)

