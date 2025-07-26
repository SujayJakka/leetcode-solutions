import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        my_dict = Counter(words)
        min_heap = []

        for word, count in my_dict.items():
            heapq.heappush(min_heap, (-count, word))

        res = []
        for _ in range(k):
            count, word = heapq.heappop(min_heap)
            res.append(word)
        
        return res
            