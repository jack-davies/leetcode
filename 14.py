class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        output = ""
        i = 0
        try:
            while True:
                char = strs[0][i]
                for string in strs:
                    if string[i] != char:
                        return output
                output += char
                i += 1
        except IndexError:
            return output
