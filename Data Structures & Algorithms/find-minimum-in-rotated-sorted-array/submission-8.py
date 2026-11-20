class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = nums[0]

        while left < right:
            mid = left + (right - left) // 2

            minimum = min(minimum, nums[mid])

            if nums[right] < nums[mid]:
                left = mid
            else:
                right = mid - 1
        return minimum

