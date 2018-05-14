class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        jump1 = (numRows - 1) * 2
        jump2 = 0
        output = s[0::jump1]
        jump1 -= 2
        jump2 += 2
        i = 1
        while jump1 != 0:
            j = i
            while j < len(s):
                output += s[j]
                j += jump1
                if j < len(s):
                    output += s[j]
                    j += jump2
            i += 1
            jump1 -= 2
            jump2 += 2
        output += s[numRows-1::jump2]
        return output
        

a = Solution()
out = a.convert("PAYPALISHIRING", 1)
print(out)
print(out == "PAHNAPLSIIGYIR")