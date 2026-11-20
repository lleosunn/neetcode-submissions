class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build character count dictionary of t string
        # dynamic sliding window
        # expand right when constraints are unsatisfied
        # shrink on the left when constraints are satisfied

        t_chars = {}
        for c in t:
            t_chars[c] = t_chars.get(c, 0) + 1

        left = 0
        min_len = float("inf")
        s_chars = {}
        start = 0

        for right in range(len(s)):
            s_chars[s[right]] = s_chars.get(s[right], 0) + 1
            #  while dictionaries are the same
            while self.compareDicts(t_chars, s_chars): 

                # find length of current substring
                current_length = right - left + 1

                # substring beats incumbent
                if current_length <= min_len: 
                    min_len = current_length
                    start = left
                
                s_chars[s[left]] -= 1
                left += 1
        return s[start:start+min_len]
                    
    
    def compareDicts(self, t_chars, s_chars):
        """Return True if dicts are the same, False otherwise"""
        for k, v in t_chars.items():
            if k not in s_chars or v > s_chars[k]:
                return False
        return True
