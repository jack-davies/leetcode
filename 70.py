class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1

        i = 1
        while i <= n:
            a, b = b, (a + b)
            i += 1

        return b
