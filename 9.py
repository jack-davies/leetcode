class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:
            return True
        
        if x < 0 or x % 10 == 0:
            return False
        
        def nth_digit(num, n, digit):
            return (num - num // math.pow(10, n-digit+1) * math.pow(10, n-digit+1)) // math.pow(10, n-digit)
            
        n_digits = math.floor(math.log(x, 10) + 1)
        for i in range(1, (n_digits // 2) + 1):
            if nth_digit(x, n_digits, i) != nth_digit(x, n_digits, n_digits-i+1):
                return False
        return True
    
a = Solution()
print(a.isPalindrome(1000030001))