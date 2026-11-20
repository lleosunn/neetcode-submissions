class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return n
        if n not in memo:
            memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]