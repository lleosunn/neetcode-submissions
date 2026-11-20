class Solution:
    def search(self, nums: List[int], target: int) -> int:
        while nums:
            middle = len(nums) % 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                nums = nums[:middle]
            else:
                nums = nums[middle + 1:]
        return -1
