class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return counter(s) == counter(t)
    
def counter(str) -> dict:
    output = {}
    for c in str:
        if c not in output:
            output[c] = 1
        else:
            output[c] += 1
    return output