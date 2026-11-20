class Solution:
    def trap(self, height: List[int]) -> int:
        pre_max = self.calcPrefixMaximum(height)
        suf_max = self.calcPrefixMaximum(reversed(height))
        out = 0
        for i, n in enumerate(height):
            out += (min(pre_max[i], suf_max[i]) - n)
        return out
            
    def calcPrefixMaximum(self, height):
        # given list, return maximum number u can see by looking to the left
        out = []
        m = 0
        for n in height:
            n = max(n, m)
            out.append(n)
        return out

