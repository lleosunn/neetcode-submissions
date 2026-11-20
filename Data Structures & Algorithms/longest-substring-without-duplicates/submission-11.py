class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict() # characters to indicies
        left_pointer = 0
        longest = 0

        for i, char in enumerate(s):
            if char in seen:
                left_pointer = seen[char] + 1
            seen[char] = i
            curr = i - left_pointer + 1
            if curr > longest:
                longest = curr
        return longest