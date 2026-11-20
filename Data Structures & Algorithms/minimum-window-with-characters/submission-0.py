class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build character count dictionary of t string
        # dynamic sliding window
        # expand right until we have at least the characters necessary
        # shrink on the left until we can't shrink anymore

        t_chars = {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1
        print(t_chars)