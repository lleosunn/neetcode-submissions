class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, j in enumerate(nums):
            if target - j in seen:
                return [i, seen[j]]
            else:
                seen[j] = i
            