class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 1
        best = (0,0)
        while i < len(s):
            offset = 1
            while i-offset >= 0 and i+offset < len(s) and s[i-offset] == s[i+offset]:
                offset += 1
            if 2 * offset - 1 > best[1] - best[0] + 1:
                best = (i-offset+1, i+offset-1)
                print(i, offset, best)
            
            if s[i-1] == s[i]:
                offset = 1
                while i-offset-1 >= 0 and i+offset < len(s) and s[i-offset-1] == s[i+offset]:
                    offset += 1
                if (2 * offset) > best[1] - best[0] + 1:
                    best = (i-offset-1+1, i+offset-1)
                    print(i, offset, best)
            i += 1
        return(s[best[0]:best[1]+1])
        
a = Solution()
print(a.longestPalindrome("cbbd"))