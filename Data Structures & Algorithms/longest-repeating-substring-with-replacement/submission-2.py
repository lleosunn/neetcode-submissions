class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # window size = k + character that appears the most

        # increment right pointer
        # increment left pointer if needed

        l = 0 # left pointer
        char_freq = {} # character frequencies in current window
        out = 0 # max window size so far (equivalent to len of longest substring)
        max_char_freq = 0


        for r in range(len(s)):
            # increment character count
            char_freq[s[r]] = char_freq.get(s[r], 0) + 1
            max_char_freq = max(max_char_freq, char_freq[s[r]])
            while r - l + 1 > max_char_freq + k:
                char_freq[s[l]] -= 1
                l += 1
                max_char_freq = max(char_freq.values())
            
            out = max(out, r - l + 1)
        
        return out

