class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # want to use a monotonically increasing stack
        stack = []
        max_area = 0

        for i in range(len(heights)):
            # there are two cases
            # case 1: stack is empty -> we would check current h and add it to stack
            # case 2: stack is not empty -> continue popping until we reach a smaller height
            #         then check the width

            while stack and stack[-1] >= heights[i]:
                stack.pop(-1)

            width = 1 if not stack else (i - stack[-1] - 1)
            max_area = max(max_area, width * heights[i])
            
            # add element condition
            if not stack or stack and heights[i] >= stack[-1]:
                stack.append(i)
            
            # print()
            
        return max_area


