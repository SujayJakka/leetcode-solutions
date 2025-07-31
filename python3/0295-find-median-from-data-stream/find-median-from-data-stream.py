class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

        heapify(self.max_heap)
        heapify(self.min_heap)
        
    def addNum(self, num: int) -> None:

        if self.max_heap and num > -self.max_heap[0]:
            heappush(self.min_heap, num)
        else:
            heappush(self.max_heap, -num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            num = -heappop(self.max_heap)
            heappush(self.min_heap, num)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            num = heappop(self.min_heap)
            heappush(self.max_heap, -num)

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()