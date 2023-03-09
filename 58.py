class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last = len(s) - 1
        while s[last] == " " and last > 0:
            last -= 1

        first = last
        while s[first] != " " and first >= 0:
            first -= 1

        return last - first
