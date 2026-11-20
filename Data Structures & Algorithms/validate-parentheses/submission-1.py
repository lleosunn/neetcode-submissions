class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {"(" : ")", "[" : "]", "{" : "}"}
        while s:
            if s[-1] == opentoclose[s[0]]:
                s = s[1:len(s) - 1]
                continue
            return False
        return True
