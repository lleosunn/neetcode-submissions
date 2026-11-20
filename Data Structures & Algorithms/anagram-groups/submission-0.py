class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = dict()
        # go through entire input list
        # create buckets of anagrams
        # buckets are dictionary with keys as anagram type and values as list of anagrams
        # we define our keys as a 26 length tuple counting the number of letters
        # return buckets as lists of strings
        for word in strs:
            key = stringToTuple(word)
            if key in buckets:
                buckets[key] += [word]
            else:
                buckets[key] = [word]
        
        return [val for val in buckets.values()]
                


def stringToTuple(word):
    out = [0] * 26
    for char in word:
        out[ord(char) - ord("a")] += 1
    return tuple(out)
