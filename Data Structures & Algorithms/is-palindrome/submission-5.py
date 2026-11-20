class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        lower = lower.strip(" ").strip(",").strip("?")
        print(lower)
        if lower == lower[::-1]:
            return True
        return False