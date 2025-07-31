import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(n1, n2) for n1, n2 in zip(nums1, nums2)]
        pairs = sorted(pairs, key=lambda p: p[1], reverse=True)

        min_heap = []
        my_sum = 0
        res = float("-inf")

        for n1, n2 in pairs:
            if len(min_heap) == k:
                min_n1 = heapq.heappop(min_heap)
                my_sum -= min_n1
            my_sum += n1
            heapq.heappush(min_heap, n1)
            if len(min_heap) == k:
                res = max(res, my_sum * n2)
        return res


                



