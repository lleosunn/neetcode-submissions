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
        min_len = len(s)
        s_chars = {}
        out = ""

        for right, c in enumerate(s):
            s_chars[c] = s_chars.get(c, 0) + 1

            for k, v in s_chars.items():
                while self.compareDicts(t_chars, s_chars): # dictionaries are the same
                    # update best string and min length
                    current_length = sum(s_chars.values())
                    if current_length < min_length: # substring beats incumbent
                        min_length = current_length
                        out = s[left:right + 1]
                    
                    left += 1
                    s_chars[c] -= 1
        return out
                    
    
    def compareDicts(self, tchars, schars):
        """Return True if dicts are the same, False otherwise"""
        for k, v in schars:
            if v != tchars:
                return False
        return True
