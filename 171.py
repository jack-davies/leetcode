class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        output = []
        for char in columnTitle:
            output.append(ord(char)-64-1)

        value = 0
        for i in range(len(output)):
            value += (output[len(output)-i-1] + 1) * (26 ** i)
        return value
