class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(s)
        print(t[-1])
        return s == t[::-1]