class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        ord("A") -> 65
        chr(65) -> "A"
        ord("Z") -> 90
        chr(90) => "Z"
        """

        result = []
        while columnNumber > 0:
            result.append((columnNumber-1) % 26)
            columnNumber = (columnNumber-1) // 26

        return "".join(map(lambda x: chr(x+65), result[::-1]))
