class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0

        for _ in range(len(heights) - 1):
            largest = max(calcArea(left, right, heights), largest)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1

        return largest
    

def calcArea(i1, i2, h):
    out = min(h[i1], h[i2]) * (i2 - i1)
    return out