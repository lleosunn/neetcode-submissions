class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict() # characters to indicies
        left_pointer = 0
        longest = 0

        for i, char in enumerate(s):
            if char in seen:
                left_pointer = max(seen[char] + 1, left_pointer)
            seen[char] = i
            longest = max(longest, i - left_pointer + 1)
        return longest
