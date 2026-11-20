class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True
            
        for word in wordDict:
            if s[0:len(word)] == word and self.wordBreak(s[len(word):], wordDict):
                return True
        return False