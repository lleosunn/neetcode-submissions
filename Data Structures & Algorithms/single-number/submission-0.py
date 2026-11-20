class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        solo = None
        for n in nums:
            if not n in seen:
                solo = n
                seen.add(n)
        return solo