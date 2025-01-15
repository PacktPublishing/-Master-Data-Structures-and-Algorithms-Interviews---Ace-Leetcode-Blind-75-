class MedianFinder:

    def __init__(self):
        self.leftHalf = []  # Max heap (invert the values for max heap behavior)
        self.rightHalf = [] # Min heap

    def addNum(self, num: int) -> None:
        if not self.leftHalf or num <= -self.leftHalf[0]:
            heapq.heappush(self.leftHalf, -num)  # Invert num for max heap
        else:
            heapq.heappush(self.rightHalf, num)
        
        # Rebalance heaps
        if len(self.leftHalf) > len(self.rightHalf) + 1:
            heapq.heappush(self.rightHalf, -heapq.heappop(self.leftHalf))
        elif len(self.rightHalf) > len(self.leftHalf):
            heapq.heappush(self.leftHalf, -heapq.heappop(self.rightHalf))

    def findMedian(self) -> float:
        if len(self.leftHalf) > len(self.rightHalf):
            return -self.leftHalf[0]
        elif len(self.rightHalf) > len(self.leftHalf):
            return self.rightHalf[0]
        else:
            return (-self.leftHalf[0] + self.rightHalf[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


#Question: https://leetcode.com/problems/find-median-from-data-stream
#Blog: https://blog.unwiredlearning.com/find-median-from-data-stream