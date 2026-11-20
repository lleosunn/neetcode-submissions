class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = dict()
        for n in nums:
            if n in numbers:
                return True
            else:
                numbers[n] = 1
        return False
        