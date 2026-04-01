class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        # elegant approach, req more comments
        # # push every new num to small max heap and pop largest small and push to large min heap
        # heapq.heappush(self.large, heapq.heappushpop_max(self.small, num))
        # # auto rebalance all odd qty sets to small max heap for faster median lookup
        # if len(self.large) > len(self.small):
        #     heapq.heappush_max(self.small, heapq.heappop(self.large))

        # long approach, more self-explanatory and readily-adaptable
        heapq.heappush_max(self.small, num)

        if (self.small and self.large) and (self.small[0] > self.large[0]):
            heapq.heappush(self.large, heapq.heappop_max(self.small))

        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, heapq.heappop_max(self.small))

        if len(self.small) + 1 < len(self.large):
            heapq.heappush_max(self.small, heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]
        # req elif for long approach
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.small[0] + self.large[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()