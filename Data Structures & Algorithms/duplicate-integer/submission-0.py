class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = dict()
        for n in nums:
            if nums[n]:
                return True
            else:
                nums[n] = 1
        return False
        