class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        largest = 0

        for _ in range(len(heights) - 2):
            # print(left, right)
            largest = max(calcArea(left, right, heights), largest)
            if heights[left + 1] > heights[right - 1]:
                left += 1
            else:
                right -= 1

        return largest
    

def calcArea(i1, i2, h):
    # print(h[i1], h[i2], i1, i2)
    out = min(h[i1], h[i2]) * (i2 - i1)
    # print(out)
    return out