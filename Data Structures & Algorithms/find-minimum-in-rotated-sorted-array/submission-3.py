class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        minimum = nums[0]

        while left <= right:
            mid = left + (right - left) // 2

            minimum = min(minimum, nums[mid])

            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid
        return minimum


        