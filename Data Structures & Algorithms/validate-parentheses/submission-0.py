class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {"(" : ")", "[" : "]", "{" : "}"}
        while s:
            if s[-1] == opentoclose[s[0]]:
                s = s[1:-2]
                continue
            return False
        return True
