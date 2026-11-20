class Solution:
    def reverseBits(self, n: int) -> int:
        return int(reversed(string(n)), 2)