class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        for word in wordDict:
            if s[0:len(word)] == word and wordBreak(s[len(word):], wordDict):
                return True
            else:
                return False
                