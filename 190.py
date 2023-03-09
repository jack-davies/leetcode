class Solution:
    def reverseBits(self, n: int) -> int:
        value = 0
        bits = "{0:b}".format(n).zfill(32)[::-1]
        for i in range(len(bits)):
            value += int(bits[len(bits)-i-1]) << i
        return value
