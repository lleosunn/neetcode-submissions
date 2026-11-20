class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = dict()
        for n in nums:
            if numbers[n] == 1:
                return True
            else:
                numbers[n] = 1
            print(numbers)
        return False
        