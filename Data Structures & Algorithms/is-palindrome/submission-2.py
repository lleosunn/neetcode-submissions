class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        lower = lower.remove(" ")
        if lower == lower[::-1]:
            return True
        return False