import heapq as hq

class MedianFinder:

    def __init__(self):
        self.small = [] # Max heap to store first half of numbers
        self.large = [] # Min heap to store second half of numbers

    def addNum(self, num: int) -> None:
        if not self.small and not self.large:
            hq.heappush(self.small, -1 * num)
        elif len(self.small) > len(self.large):
            if self.small[0] > num:
                hq.heappush(self.large, -1 * hq.heappop(self.small))
                hq.heappush(self.small, -1 * num)
            else:
                hq.heappush(self.large, num)
        else:
            if self.large[0] < num:
                hq.heappush(self.small, -1 * hq.heappop(self.large))
                hq.heappush(self.large, num)
            else:
                hq.heappush(self.small, -1 * num)

    def findMedian(self) -> float:
        if len(self.small) < len(self.large):
            return self.large[0]
        elif len(self.small) > len(self.large):
            return -1 * self.small[0]
        else: return (-1 * self.small[0] + self.large[0]) / 2        
        