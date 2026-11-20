class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        out = 0
        while l < r:
            if left_max < right_max:
                out += left_max - height[l]
                l += 1
                left_max = max(height[l], left_max)
            else:
                out += right_max - height[r]
                r -= 1
                right_max = max(height[r], right_max)
        return out