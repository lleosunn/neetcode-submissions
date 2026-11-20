class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)
        largest = 0

        for _ in range(len(heights)):
            print(left, right)
            largest = max(calcArea(left, right, heights), largest)
            if heights[left + 1] > heights[right - 1]:
                left += 1
            else:
                right -= 1
    

def calcArea(i1, i2, heights):
    return max(heights[i1], heights[i2]) * (i2 - i1)