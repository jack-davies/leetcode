class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        output = 0
        prev = 0
        for char in reversed(s):
            current = values[char]
            if current >= prev:
                output += current
            else:
                output -= current
            prev = current
        return output
        
a = Solution()
print(a.romanToInt("MCMXCIV"))