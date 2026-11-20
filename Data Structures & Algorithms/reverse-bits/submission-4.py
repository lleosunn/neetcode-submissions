class Solution:
    def reverseBits(self, n: int) -> int:
        return int(reversed(str(n)), 2)