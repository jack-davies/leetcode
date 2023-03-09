class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        digits = [["", "M", "MM", "MMM"],
                  ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
                  ["", "X", "XX" ,"XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
                  ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]]
        num = str(num)
        num = "0" * (4 - len(num)) + num
        output = ""
        for i, char in enumerate(num):
            output += digits[i][int(char)]
        return output
