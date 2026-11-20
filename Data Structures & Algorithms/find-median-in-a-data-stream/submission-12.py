import heapq as hq

class MedianFinder:

    def __init__(self):
        self.small = [] # max heap 
        self.big = [] # min heap

    def addNum(self, num: int) -> None:
        hq.heappush(self.small, -num)
        hq.heappush(self.big, -hq.heappop(self.small))
        if len(self.big) > len(self.small):
            hq.heappush(self.small, -hq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        else:
            return (self.big[0] - self.small[0]) / 2
        
        