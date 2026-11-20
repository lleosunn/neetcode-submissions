class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # order of nums doesn't matter, just whats inside it
        # setify nums
        # now we have set of unordered
        # check if a start is a start and count up
        nums = set(nums)
        longest = 1
        for n in nums:
            if n - 1 in nums: # n is not a start
                continue
            else:
                # n is a start
                count = 1
                while n in nums:
                    count += 1
                    n += 1
                longest = max(count, longest)
        return longest

    