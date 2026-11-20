class Solution:
    def reverseBits(self, n: int) -> int:
        return int("0b"+str(reversed(str(n))), 2)