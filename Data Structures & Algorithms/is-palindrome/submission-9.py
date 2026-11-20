class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        valid = 'abcdefghijklmnopqrstuvwxyz0123456789'
        new = ""
        for char in lower:
            if char in valid:
                new = new+char
        if new == new[::-1]:
            return True
        return False