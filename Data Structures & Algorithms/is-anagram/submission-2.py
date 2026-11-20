class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s)
        print(t)
        return s == t[::-1]