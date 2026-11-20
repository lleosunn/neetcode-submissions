class Solution:
    def isValid(self, s: str) -> bool:
        opentoclose = {"(" : ")", "[" : "]", "{" : "}"}
        while len(s) > 0:
            if opentoclose[s[0]] == s[-1]:
                s = s[1:len(s) - 1]
            else:
                return False
        return True
