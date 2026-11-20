class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        counter = 0
        for char in s:
            if char in seen:
                seen = set()
                if counter > longest:
                    longest = counter
                counter = 0
            seen.add(char)
            counter += 1
        return longest