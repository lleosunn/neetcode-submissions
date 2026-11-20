class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        # loop for n+1 because if no indices get popped, still want to calculate area
        for i in range(n + 1):

            # pop until current height is greater than the last element
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]

                # check area
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea