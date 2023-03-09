class Solution:
    def mySqrt(self, x: int) -> int:
        def square(n):
            return n * n

        i, j, offset = 0, 1, 0

        while square(offset + j) <= x:
            while square(offset + j) <= x:
                i = j
                j *= 2
            offset = offset + i
            i = 0
            j = 1

        return offset
