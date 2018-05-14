class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        output = ""
        for idx, char in enumerate(str):
            if char == " ":
                pass
            elif char == "-" or char == "+" or (ord(char) > 47 and ord(char) < 58):
                output += char
                i = idx + 1
                break
            else:
                return 0
        
        while i < len(str) and (ord(str[i]) > 47 and ord(str[i]) < 58):
            output += str[i]
            i += 1
        
        if output == "" or output == "-" or output == "+":
            return 0
        
        output = int(output)
        
        if output < -2147483648:
            return -2147483648
        if output > 2147483647:
            return 2147483647
        return output
    
a = Solution()
print(a.myAtoi("42"))
print(a.myAtoi("   -42"))
print(a.myAtoi("4193 with words"))
print(a.myAtoi("words and 987"))
print(a.myAtoi("-91283472332"))
print(a.myAtoi(""))
print(a.myAtoi("-"))