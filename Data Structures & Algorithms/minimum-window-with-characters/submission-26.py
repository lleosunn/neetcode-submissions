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
        debug = False

        for right in range(len(s) + 1):

            s_chars[s[right]] = s_chars.get(s[right], 0) + 1
            if debug: print(s_chars, self.compareDicts(t_chars, s_chars))
            #  while dictionaries are the same
            while self.compareDicts(t_chars, s_chars): 

                # find length of current substring
                current_length = sum(s_chars.values())

                # substring beats incumbent
                if current_length < min_len: 
                    min_length = current_length
                    out = s[left:right + 1]
                
                # print(s_chars, s[left])
                s_chars[s[left]] -= 1
                left += 1
            if right == 7: debug = False
            
        return out
                    
    
    def compareDicts(self, t_chars, s_chars):
        """Return True if dicts are the same, False otherwise"""
        for k, v in t_chars.items():
            if k not in s_chars or v != s_chars[k]:
                return False
        return True
