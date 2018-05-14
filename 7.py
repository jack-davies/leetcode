class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            output = -int(str(x)[:0:-1])
        else:
            output = int(str(x)[::-1])
        if output > 2147483647 or output < -2147483648:
            return 0
        return output
        


a = Solution()
print(a.reverse(-2147483648))