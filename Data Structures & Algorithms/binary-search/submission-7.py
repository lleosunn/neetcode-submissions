class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = 0
        while nums:
            middle = len(nums) // 2
            if nums[middle] == target:
                return middle + index
            elif nums[middle] > target:
                nums = nums[:middle]
            else:
                nums = nums[middle + 1:]
                index += middle
        return -1
