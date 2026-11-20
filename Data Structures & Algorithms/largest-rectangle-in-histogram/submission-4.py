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

            if not stack:
                max_area = max(heights[i], max_area)
                stack.append(i)
            else:
                while stack and stack[-1] >= heights[i]:
                    stack.pop(-1)
                # no more elements:
                if not stack:
                    max_area = max(max_area, (i-1) * heights[i])
                else:
                    max_area = max(max_area, (i - stack[-1] - 1) * heights[i])
            
            print(stack)
            
        return max_area


