class Solution:
    def reverseBits(self, n: int) -> int:
        return int("ob"+reversed(str(n)), 2)