class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = dict() # characters to indicies
        left_pointer = 0
        longest = 0

        for i in range(len(s)):
            if s[i] in seen:
                left_pointer = max(seen[s[i]] + 1, left_pointer)
            seen[s[i]] = i
            longest = max(longest, i - left_pointer + 1)
        return longest
