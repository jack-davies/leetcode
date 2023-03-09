class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        j = -1
        current = 0
        record = 0
        encountered = set()
        while j+1 < len(s):
            j += 1
            while s[j] in encountered:
                encountered.remove(s[i])
                i += 1
                current -= 1
            encountered.add(s[j])
            current += 1
            record = max(current, record)
        return record
