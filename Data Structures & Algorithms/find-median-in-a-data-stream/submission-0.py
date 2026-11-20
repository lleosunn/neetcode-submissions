class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()

    def findMedian(self) -> float:
        size = len(self.arr)
        odd = size % 2
        if odd: return self.arr[size // 2]
        else: return (self.arr[size / 2 - 1] + self.arr[size / 2]) / 2
        